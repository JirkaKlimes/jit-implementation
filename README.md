# JIT Implementation: Just-in-Time Code Generation

## You've heard of Just-in-Time Compilation. Now, get ready for Just-in-Time Implementation!

Tired of writing code? Wish your programs could write themselves? Look no further! JIT Implementation is here to revolutionize your development process!

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

-   **100% IDE Support**: Works flawlessly with all IDEs, even the ones that don't exist yet!
-   **Lazy Implementation**: Why write code when you can let an AI do it for you?
-   **Context-Aware**: Analyzes your codebase to understand custom types and project structure. It's like having a mind reader for your code!
-   **Test-Driven Development**: Provide test cases, and watch JIT Implementation pass them. Because even AI needs a reality check sometimes.
-   **Smart Caching**: Stores generated implementations for reuse. It's like a squirrel, but for code!
-   **100% Reproducible**: With LLM sampling temperature set to 0, it's more consistent than your coffee order.
-   **Dynamic Generation**: Creates code on-the-fly based on signatures and docstrings. It's like watching code grow in fast-forward!
-   **In-Place Rewriting**: Option to modify source files directly. Watch your TODOs turn into DONEs automagically!

### Installation

```bash
pip install jit-implementation
```

### Usage

Behold, possibly the world's shortest implementation of a GUI Snake game:

```python
from jit_implementation import implement

@implement
class Snake:
    """Pygame-based Snake game. Initializing launches the game."""

if __name__ == "__main__":
    Snake()

# Congratulations! You've just created a fully functional Snake game in just 3 lines of code!
```

Yes, it actually works! Who needs hundreds of lines of code when you have JIT Implementation?

Here's another example for the more practically minded:

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

1. You provide a function or class signature with a docstring.
2. JIT Implementation analyzes your codebase, including custom types and classes.
3. This information is sent to an LLM along with your project context.
4. The LLM generates an implementation, complete with a "Chain of Thought" explanation.
5. JIT Implementation runs your tests (if provided) and iterates if necessary.
6. The generated code is cached in `.jit_impl` for future use, including metadata like version, timestamp, test results, original filename, implementation checksum, and chain of thought.

### Warning

While JIT Implementation is an interesting experiment, please use responsibly:

-   Generated code may not always be optimal or secure.
-   Review and understand any code before using it in production.
-   Overreliance on automated generation can hinder learning and problem-solving skills.

## Disclaimer

This project is primarily for educational and experimental purposes. It should not be relied upon for critical or production systems without thorough review and testing. Also, if your AI-generated code becomes sentient, we're not responsible for the robot uprising.

## License

MIT License - Because even experimental projects need a license. Feel free to use, modify, and distribute this code at your own risk. We're not responsible for any sentient AIs that may result from its use.

## TODO

-   [ ] Implement package management (requirements.txt, poetry)
-   [ ] Add support for implementing class methods and properties
-   [ ] Automatically add and verify imports for used types
-   [ ] Improve error handling for test execution
-   [ ] Add support for multiple LLM providers (claude, ollama)

## Support the Project

If you find JIT Implementation helpful or amusing, consider buying me a coffee! Your support helps keep the AI well-caffeinated and the code flowing.

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jiriklimes)

---

Remember: JIT Implementation is here to assist and amuse, not to replace human developers. Use it wisely, and don't forget to laugh along the way!

_"The best code is the code you never had to write." - Anonymous JIT Implementation User_
