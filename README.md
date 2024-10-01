# JIT Implementation: Just-in-Time Code Generation

## You've heard of Just-in-Time Compilation. Now, get ready for Just-in-Time Implementation!

Tired of writing code? Wish your programs could write themselves? Look no further! JIT Implementation is here to revolutionize your development process.

### What is JIT Implementation?

JIT Implementation is a groundbreaking Python library that generates your functions and classes on the fly using the power of Large Language Models (LLMs). Simply decorate your function or class with `@implement`, and watch the magic unfold!

```python
from jit_implementation import implement

@implement
def solve_world_hunger():
    """Solve world hunger"""

# Congratulations! You've just solved world hunger!
```

### Features

-   **Lighter Builds**: Enjoy lighter builds since the code isn't even there until you need it.
-   **Lazy Implementation**: Code is dynamically created at the point of necessity, reducing overhead.
-   **100% Reproducible**: With LLM sampling temperature set to 0, results are consistent.
-   **Context-Aware**: Analyzes your codebase to understand custom types and project structure.
-   **Test-Driven Development**: Provide test cases, and JIT Implementation ensures they pass.
-   **Smart Caching**: Stores generated implementations for reuse.
-   **In-Place Rewriting**: Option to modify source files directly.

### Installation

```bash
pip install jit-implementation
```

### Usage

Behold, a minimalist implementation of a GUI Snake game:

```python
from jit_implementation import implement

@implement
class Snake:
    """Pygame-based Snake game. Initializing launches the game."""

if __name__ == "__main__":
    Snake()

# You've just created a fully functional Snake game in just a few lines of code!
```

Yes, it actually works! Who needs hundreds of lines of code when you have JIT Implementation?

Here's another practical example:

```python
from typing import List
from jit_implementation import implement

@implement(
    test_functions=[
        lambda f: (f(100) == [2, 2, 5, 5], "Prime factors of 100"),
    ]
)
def prime_factors(n: int) -> List[int]:
    """Return the prime factors of n"""

# Now you can use prime_factors as if you had implemented it yourself!
assert prime_factors(100) == [2, 2, 5, 5]
assert prime_factors(69420) == [2, 2, 3, 5, 13, 89]
```

### How It Works

1. **Define**: You provide a function or class signature with a docstring.
2. **Analyze**: JIT Implementation analyzes your codebase, including custom types and classes.
3. **Generate**: This information is sent to an LLM along with your project context.
4. **Iterate**: The LLM generates an implementation, complete with a "Chain of Thought" explanation.
5. **Validate**: JIT Implementation runs your tests (if provided) and iterates if necessary.
6. **Cache**: The generated code is cached in `.jit_impl` for future use, including metadata like version, timestamp, test results, original filename, implementation checksum, and chain of thought.

### Warning

While JIT Implementation is a powerful tool, please use responsibly:

-   **Review Generated Code**: The generated code may not always be optimal or secure. Always review and understand any code before using it in production.
-   **Security Considerations**: Be cautious of potential security vulnerabilities in auto-generated code.
-   **Learning Curve**: Overreliance on automated generation can hinder learning and problem-solving skills.

## Disclaimer

This project is primarily for educational and experimental purposes. It should not be relied upon for critical or production systems without thorough review and testing.

## License

MIT License. Feel free to use, modify, and distribute this code at your own risk.

## TODO

-   [ ] Implement package management (requirements.txt, poetry)
-   [ ] Add support for implementing class methods and properties
-   [ ] Automatically add and verify imports for used types
-   [ ] Improve error handling for test execution
-   [ ] Add support for multiple LLM providers (Claude, Ollama)

## Support the Project

If you find JIT Implementation helpful or funny, consider buying me a coffee! Your support helps keep the development going.

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jiriklimes)

---

Remember: JIT Implementation is here to assist, not to replace human developers. Use it wisely, and enjoy the efficiency it brings!

_"The best code is the code you didn't have to write." - Anonymous JIT Implementation User_
