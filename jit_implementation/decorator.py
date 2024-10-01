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
    def decorator(obj: Callable):
        coder = Coder(obj, test_functions, autonomous, in_place, max_tries)
        obj = coder.run()
        return obj

    return decorator(obj) if callable(obj) else decorator
