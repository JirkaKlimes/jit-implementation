from typing import List
from jit_code.decorator import implement


@implement(
    test_functions=[
        lambda f: (f(100) == [2, 2, 5, 5], "Prime factors of 100"),
    ]
)
def prime_factors(n: int) -> List[int]:
    """Return the prime factors of n"""


if __name__ == "__main__":
    assert prime_factors(100) == [2, 2, 5, 5]
    assert prime_factors(69420) == [2, 2, 3, 5, 13, 89]
