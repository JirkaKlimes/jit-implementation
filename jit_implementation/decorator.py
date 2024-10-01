from typing import Any, Callable, List, Tuple
from jit_implementation.coder import Coder


def implement(
    obj: Callable | None = None,
    /,
    *,
    test_functions: List[Callable[[Any], Tuple[bool, str]]] = None,
    autonomous: bool = True,
    in_place: bool = False,
    max_tries: int = 5,
):
    """
    A decorator that implements the decorated function or class just-in-time using AI-powered code generation.

    This decorator uses a Large Language Model to generate an implementation based on the function
    signature, docstring, and optional test cases. It can be used to quickly prototype functions
    or create placeholder implementations that pass specified tests.

    Parameters:
    -----------
    test_functions : List[Callable[[Any], Tuple[bool, str]]], optional
        A list of test functions to validate the implementation. Each function should take
        the implemented object as an argument and return a tuple of (bool, str), where the
        bool indicates if the test passed and the str is a description of the test.
    autonomous : bool, default=True
        If True, the implementation will be generated without user interaction. If False,
        the user may be prompted for input during the implementation process.
    in_place : bool, default=False
        If True, the source file of the decorated object will be modified to include the
        generated implementation. If False, the implementation will be stored separately.
    max_tries : int, default=5
        The maximum number of attempts to generate a valid implementation that passes all tests.

    Notes:
    ------
    - The quality and correctness of the implementation depend on the clarity of the
      function signature, docstring, and provided test cases.
    - Use this decorator responsibly and always review and test the generated code
      before using it in production environments.
    """

    def decorator(obj: Callable):
        coder = Coder(obj, test_functions, autonomous, in_place, max_tries)
        obj = coder.run()
        return obj

    return decorator(obj) if callable(obj) else decorator
