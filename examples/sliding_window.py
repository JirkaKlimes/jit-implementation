from typing import List
from jit_code.decorator import implement


@implement
def sliding_window(sequence: List[int], window_size: int) -> List[List[int]]:
    """Create a sliding window of the given size over the sequence."""


if __name__ == "__main__":
    assert sliding_window([1, 2, 3, 4, 5], 3) == [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    assert sliding_window([1, 2, 3, 4, 5], 4) == [[1, 2, 3, 4], [2, 3, 4, 5]]
