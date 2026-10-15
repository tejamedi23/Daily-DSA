"""
Day 01 — Arrays: Find the Largest Element

Approach:
1. Treat the first element as the current largest.
2. Scan each remaining element once.
3. Update the largest value whenever a bigger element appears.

Time complexity: O(n) — each element is checked once.
Auxiliary space: O(1) — only one extra variable is maintained.
"""


def find_largest(numbers: list[int]) -> int:
    """Return the largest integer in a non-empty list."""
    if not numbers:
        raise ValueError("The array must not be empty")

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest


def run_tests() -> None:
    """Test typical inputs and important edge cases."""
    assert find_largest([12, 5, 28, 9, 17]) == 28
    assert find_largest([-8, -3, -12, -1]) == -1
    assert find_largest([7]) == 7
    assert find_largest([4, 4, 4]) == 4

    try:
        find_largest([])
    except ValueError:
        pass
    else:
        raise AssertionError("An empty list should raise ValueError")

    print("All tests passed!")


if __name__ == "__main__":
    values = [12, 5, 28, 9, 17]
    print("Array:", values)
    print("Largest element:", find_largest(values))
    run_tests()
