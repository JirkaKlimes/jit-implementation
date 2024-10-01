import enum
import inspect
import os
import re
import subprocess
import sys
import tempfile
import hashlib
from typing import Any, Callable, ClassVar, List, Tuple
from pathlib import Path
import datetime as dt

from jinja2 import Template
import openai
from pydantic import BaseModel, Field
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text

from jit_implementation.ide import IDE

REVISION_TEMPLATE = Template("""\
# Version: {{ version }} - Generated on {{ timestamp }}

# Tests Passed: {{ tests_passed }}

# Declaration File: {{ declaration_file }}
# Implementation Checksum: {{ implementation_checksum }}

{% if chain_of_thought %}
# Chain of Thought:
# {{ chain_of_thought }}
{% endif %}

{% if imports %}
# Imports
{{ imports }}
{% endif %}

# Implementation
{{ code }}
""")


class StrEnum(str, enum.Enum):
    def _generate_next_value_(name, *_):
        return name

    def __str__(self):
        return str.__str__(self)


class SubmitVersion(BaseModel):
    imports: List[str] = Field(..., description="Required imports")
    code: str = Field(..., description="Code of the object (without import statements)")


class Reasoning(BaseModel):
    chain_of_thought: List[str] = Field(..., description="Chain of thought")


class Coder:
    PROMPT: ClassVar[str] = (
        "You are a senior developer tasked with implementing Python functions and classes.\n"
        "Follow these guidelines to produce high-quality, efficient, and maintainable code:\n"
        "\n"
        "1. Code Structure and Organization:\n"
        "   - Separate imports and code:\n"
        "     * Place all import statements in the 'imports' field.\n"
        "     * Put implementation code in the 'code' field, excluding import statements.\n"
        "   - Use meaningful names for variables, functions, and classes.\n"
        "\n"
        "2. Performance Optimization:\n"
        "   - Optimize for lowest time and space complexity.\n"
        "   - Use appropriate data structures (e.g., sets for membership testing, dictionaries for fast lookups).\n"
        "   - Employ efficient algorithms and avoid unnecessary computations.\n"
        "\n"
        "3. Code Quality and Readability:\n"
        "   - Follow PEP 8 style guide for Python code.\n"
        "   - Write self-documenting code with clear and concise variable and function names.\n"
        "   - Add comments for complex logic or non-obvious implementation details.\n"
        "   - Use type hints to improve code clarity and catch potential type-related errors.\n"
        "\n"
        "Remember: Write code that is not only functional but also maintainable and scalable."
    )
    IMPLEMENTATION_PATH: ClassVar[Path] = Path(".jit_impl")
    API_KEY: ClassVar[str] = None
    MODEL: ClassVar[str] = "gpt-4o-2024-08-06"
    TEMPERATURE: ClassVar[float] = 0.0

    def __init__(
        self,
        obj: Any,
        test_functions: List[Callable[[Any], Tuple[bool, str]]] = None,
        autonomous: bool = True,
        in_place: bool = False,
        max_tries: int = 5,
    ):
        self.obj = obj
        self.test_functions = test_functions or []
        self.autonomous = autonomous
        self.in_place = in_place
        self.max_tries = max_tries

        self.console = Console()
        self.ide = IDE(self.obj)

    @property
    def oai(self):
        api_key = self.API_KEY or os.getenv("OPENAI_API_KEY")
        if not api_key:
            self.console.print(
                "[bold red]OPENAI_API_KEY environment variable not set. Exiting...[/bold red]"
            )
            quit()
        return openai.Client(api_key=api_key)

    @property
    def code_path(self) -> Path:
        directory = self.IMPLEMENTATION_PATH / Path(
            inspect.getfile(self.obj).replace(".py", "")
        ).relative_to(Path.cwd())
        directory.mkdir(parents=True, exist_ok=True)
        return directory / f"{self.obj.__name__}.py"

    def _format_code(self, code: str) -> str:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False
        ) as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name

        try:
            self.console.print("Running Ruff to format code...")
            subprocess.run(
                ["ruff", "format", temp_file_path], check=True, capture_output=True
            )
            with open(temp_file_path, "r") as fixed_file:
                fixed_code = fixed_file.read()
            return fixed_code
        except subprocess.CalledProcessError as e:
            self.console.print(
                f"[bold red]Ruff encountered an error:[/bold red] {e.stderr.decode()}"
            )
            return code
        except FileNotFoundError:
            self.console.print(
                "[bold red]Ruff is not installed or not in PATH[/bold red]"
            )
            return code
        finally:
            os.unlink(temp_file_path)

    def _print_code(self, title: str, code: str):
        self.console.print(
            Panel(
                Syntax(code, "python", theme="monokai", line_numbers=True), title=title
            )
        )

    def _print_llm_output(self, message: str):
        self.console.print(Text(message, style="bold cyan"))

    def _compile_code(self, code: str) -> Any:
        compiled_code = compile(code, "<string>", "exec")
        namespace = {}
        exec(compiled_code, namespace)
        return namespace[self.obj.__name__]

    def _remove_duplicate_imports(self, code: str) -> str:
        pattern = r"^\s*(import .*|from .* import .*)$"
        return re.sub(pattern, "", code, flags=re.MULTILINE).strip()

    def _get_implementation_checksum(self) -> str:
        declaration_source = inspect.getsource(self.obj)
        tests_str = "\n".join(inspect.getsource(func) for func in self.test_functions)
        return hashlib.sha256(f"{declaration_source}{tests_str}".encode()).hexdigest()

    def _should_reuse_code(self, implementation_checksum: str) -> bool:
        if not self.code_path.exists():
            return False

        with open(self.code_path, "r") as f:
            content = f.read()

        existing_hash = re.search(r"Implementation Checksum: (\w+)", content)

        return existing_hash and existing_hash.group(1) == implementation_checksum

    def run(self):
        implementation_checksum = self._get_implementation_checksum()

        if self._should_reuse_code(implementation_checksum):
            return self._compile_code(self.code_path.read_text())

        self._print_code(
            "Callable to implement",
            self.ide.read_source(
                self.obj,
                postprocessor=lambda code: re.sub(
                    r"^(?:@[\s\S]*?(?:\n|$))*(?=\s*(?:def|class)\s)",
                    "",
                    code,
                    flags=re.MULTILINE,
                ),
            ),
        )

        messages = [
            {"role": "system", "content": self.PROMPT},
            {
                "role": "user",
                "content": f"Implement the following function or class in Python.\n"
                f"Please remember to separate imports and code as per instructions.\n"
                f"Function or class to implement:\n{self.ide.read_source(self.obj)}",
            },
        ]

        tools = [
            openai.pydantic_function_tool(SubmitVersion),
            openai.pydantic_function_tool(Reasoning),
        ]

        version = 0
        chain_of_thought = []
        tries = 0

        while tries < self.max_tries:
            if not self.autonomous and tries > 0:
                if not self._prompt_continue():
                    self.console.print("[yellow]Operation cancelled by user.[/yellow]")
                    return None

            current_tools = tools.copy()

            if self.ide.unread_types:
                _types = StrEnum("types", [t.__name__ for t in self.ide.unread_types])

                class ReadSourceCode(BaseModel):
                    type: _types  # type: ignore

                current_tools.append(openai.pydantic_function_tool(ReadSourceCode))

            response = self.oai.beta.chat.completions.parse(
                messages=messages,
                model=self.MODEL,
                tool_choice="required",
                tools=current_tools,
                temperature=self.TEMPERATURE,
            )

            message = response.choices[0].message
            messages.append(message)

            for call in message.tool_calls:
                if isinstance(call.function.parsed_arguments, Reasoning):
                    chain_of_thought.extend(
                        call.function.parsed_arguments.chain_of_thought
                    )
                    self._print_llm_output("Chain of thought:")
                    self.console.print(
                        "\n".join(call.function.parsed_arguments.chain_of_thought)
                    )
                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": call.id,
                            "content": "valid",
                        }  # WTF do I return?
                    )

                elif self.ide.unread_types and isinstance(
                    call.function.parsed_arguments, ReadSourceCode
                ):
                    self._print_llm_output(
                        f"Reading source code of type: {call.function.parsed_arguments.type}"
                    )
                    source_code = self.ide.read_source(
                        {t.__name__: t for t in self.ide.unread_types}[
                            call.function.parsed_arguments.type
                        ]
                    )
                    self._print_code(
                        f"Source of {call.function.parsed_arguments.type}", source_code
                    )
                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": call.id,
                            "content": source_code,
                        }
                    )

                elif isinstance(call.function.parsed_arguments, SubmitVersion):
                    version += 1
                    implementation = call.function.parsed_arguments
                    imports = implementation.imports
                    code = self._format_code(implementation.code)
                    code = self._remove_duplicate_imports(code)

                    self._print_code(
                        f"Implementation Version {version}",
                        "\n".join(imports) + "\n\n" + code,
                    )

                    full_code = "\n".join(imports) + "\n\n" + code
                    obj = self._compile_code(full_code)

                    failed = False
                    for case in self.test_functions:
                        passed, doc = case(obj)
                        self.console.print(
                            f"Test case `{doc}`: {'[green]PASSED[/green]' if passed else '[red]FAILED[/red]'}"
                        )
                        failed = failed or not passed

                    code_path = (
                        self.code_path
                        if not failed
                        else self.code_path.with_suffix(f".v{version:02d}_failed.py")
                    )

                    with open(code_path, "w") as f:
                        f.write(
                            REVISION_TEMPLATE.render(
                                version=version,
                                timestamp=dt.datetime.now(dt.UTC).strftime(
                                    "%Y-%m-%dT%H:%M:%SZ"
                                ),
                                tests_passed="PASSED" if not failed else "FAILED",
                                declaration_file=inspect.getfile(self.obj),
                                implementation_checksum=implementation_checksum,
                                imports="\n".join(imports),
                                chain_of_thought="# ".join(
                                    "\n".join(chain_of_thought).splitlines(True)
                                ),
                                code=code,
                            )
                        )

                    if self.in_place and not failed:
                        file = inspect.getfile(self.obj)
                        with open(file) as f:
                            source = f.read()
                        source = source.replace(inspect.getsource(self.obj), code)

                        with open(file, "w") as f:
                            f.write(source)

                        self.console.print(
                            "[green]Code updated in place. Restarting script...[/green]"
                        )
                        subprocess.Popen([sys.executable, *sys.argv])
                        sys.exit()

                    if not failed:
                        return obj
                    else:
                        tries += 1
                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": call.id,
                                "content": "Tests failed",
                            }
                        )
                        if tries >= self.max_tries:
                            raise NotImplementedError(
                                f"Maximum number of tries ({self.max_tries}) reached without passing tests."
                            )

    def _prompt_continue(self) -> bool:
        response = input("Continue to next iteration? (yes/no): ").strip().lower()
        return response.lower() in ["yes", "y", "continue"]
