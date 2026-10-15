"""
Day 01 — Find the Largest Element
---------------------------------
Given a non-empty list of numbers, return the largest element.

Example:
    Input:  [12, 5, 28, 9, 17]
    Output: 28

Complexity:
    Time:  O(n) — each element is checked once.
    Space: O(1) — only one extra variable is used.
"""


def find_largest(numbers):
    """Return the largest number in a non-empty list."""
    if not numbers:
        raise ValueError("The list must not be empty.")

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest


def test_find_largest():
    assert find_largest([12, 5, 28, 9, 17]) == 28
    assert find_largest([-8, -2, -15]) == -2
    assert find_largest([4]) == 4
    assert find_largest([3, 3, 3]) == 3

    try:
        find_largest([])
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for an empty list.")

    print("All tests passed!")


if __name__ == "__main__":
    values = [12, 5, 28, 9, 17]
    print("Input:", values)
    print("Largest element:", find_largest(values))
    test_find_largest()
