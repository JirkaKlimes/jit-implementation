from jit_code import implement


@implement
def fib(n: int) -> int: ...


if __name__ == "__main__":
    assert fib(10) == 55
