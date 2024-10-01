# JIT Code: Just-in-Time Implementation

## You've heard of Just-in-Time Compilation. Now, get ready for Just-in-Time Implementation!

Are you tired of writing your own code? Wish your programs could write themselves? Look no further! JIT Code is here to revolutionize your development process!

### What is JIT Code?

JIT Code is a groundbreaking Python library that implements your functions and classes on the fly using the power of Large Language Models (LLMs). Simply decorate your function or class with `@implement`, and watch as the magic happens!

```python
from jit_code import implement

@implement
def solve_world_hunger():
    """Solve world hunger"""

# Congratulations! You've just solved world hunger!
```

### Features

-   **Lazy Implementation**: Why write code when you can let an AI do it for you?
-   **Test-Driven Development**: Provide test cases, and JIT Code will make sure your implementation passes them.
-   **Autonomous Mode**: Set it and forget it! JIT Code will keep trying until it gets it right.
-   **In-Place Rewriting**: Want to see the implemented code? Use `in_place=True` and watch your source files transform!
-   **Smart Caching**: When `in_place=False`, implementations are stored in `.jit_code` and reused if the checksum hash matches.

### Installation

```bash
pip install jit-code
```

### Usage

Behold, possibly the world's shortest implementation of a GUI Snake game:

```python
from jit_code import implement

@implement
class Snake:
    """Pygame-based Snake game. Initializing launches the game."""

if __name__ == "__main__":
    Snake()

# Congratulations! You've just created a fully functional Snake game in just 3 lines of code!
```

Yes, it actually works! Who needs hundreds of lines of code when you have JIT Code?

Here's another example for the more practically minded:

```python
from typing import List
from jit_code import implement

@implement(
    test_functions=[
        lambda f: (f(100) == [2, 2, 5, 5], "Prime factors of 100"),
    ]
)
def prime_factors(n: int) -> List[int]:
    """Return the prime factors of n"""
    pass

# Now you can use prime_factors as if you had implemented it yourself!
assert prime_factors(100) == [2, 2, 5, 5]
assert prime_factors(69420) == [2, 2, 3, 5, 13, 89]
```

### Features

-   **100% IDE Support**: Works flawlessly with all IDEs, even the ones that don't exist yet!
-   **Smaller Builds**: Your builds will be lighter than air, thanks to code that's not even there!
-   **Context-Aware**: Analyzes your existing codebase to understand custom types and project structure. It's like having a mind reader for your code!
-   **Test-Driven Development**: Supports test functions to ensure correct implementation. Because even AI needs a reality check sometimes.
-   **Caching Mechanism**: Stores generated implementations for reuse. It's like a squirrel, but for code!
-   **100% Reproducible**: With LLM sampling temperature set to 0, it's more consistent than your coffee order. "I'll have the usual," but for code!
-   **Dynamic Implementation**: Generates code on-the-fly based on function signatures and docstrings. It's like watching code grow in fast-forward!
-   **In-Place Rewriting**: Option to modify source files directly with implemented code. Watch your TODOs turn into DONEs automagically!

### How It Works

1. You provide a function or class signature with a docstring.
2. JIT Code analyzes your codebase, including any custom types or classes you've defined.
3. This information is sent to an LLM along with the context of your project.
4. The LLM generates an implementation, complete with a "Chain of Thought" explanation.
5. JIT Code runs your tests (if provided) and repeats steps 3-4 if necessary.
6. The implemented code is cached in `.jit_code` for future use, including metadata like:
    - Version number
    - Generation timestamp
    - Test results
    - Original declaration filename
    - Implementation checksum
    - Chain of thought explanation

### Warning

While JIT Code is an interesting experiment, please use responsibly. Remember that:

-   Generated code may not always be optimal or secure.
-   It's important to review and understand any code before using it in production.
-   Overreliance on automated code generation can hinder learning and problem-solving skills.

## Disclaimer

This project is primarily for educational and experimental purposes. While it can generate functional code, it should not be relied upon for critical or production systems without thorough review and testing. Also, if your AI-generated code becomes sentient, we're not responsible for the robot uprising.

## License

MIT License - Because even joke projects need a license. Feel free to use, modify, and distribute this code at your own risk. We're not responsible for any sentient AIs that may result from its use.

---

Remember: JIT Code is here to assist and amuse, not to replace human developers. Use it wisely, and don't forget to laugh along the way!

_"The best code is the code you never had to write." - Anonymous JIT Code User_
