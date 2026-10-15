"""
Day 01 — Find the Largest Element

Approach:
Start with the first element as the current maximum. Scan the remaining
elements and update the maximum whenever a larger value is found.

Time complexity: O(n), where n is the number of elements.
Auxiliary space: O(1).
"""


def find_largest(numbers):
    """Return the largest value in a non-empty list."""
    if not numbers:
        raise ValueError("The array must not be empty")

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest


if __name__ == "__main__":
    values = [12, 5, 28, 9, 17]
    print("Array:", values)
    print("Largest element:", find_largest(values))
