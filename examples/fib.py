from jit_implementation import implement


@implement
def fib(n: int) -> int: ...


if __name__ == "__main__":
    assert fib(10) == 55
    assert fib(100) == 354_224_848_179_261_915_075
