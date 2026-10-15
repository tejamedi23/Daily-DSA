"""
Day 02 — Strings: Reverse a String

Approach:
Use Python slicing with a step of -1 to read the string from end to start.

Time complexity: O(n), where n is the length of the string.
Auxiliary space: O(n), because the reversed string is a new string.
"""


def reverse_string(text: str) -> str:
    """Return text with its characters in reverse order."""
    return text[::-1]


def run_tests() -> None:
    """Test normal inputs and edge cases."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("DSA") == "ASD"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("racecar") == "racecar"
    assert reverse_string("hello world") == "dlrow olleh"

    print("All tests passed!")


if __name__ == "__main__":
    sample = "hello"
    print("Original:", sample)
    print("Reversed:", reverse_string(sample))
    run_tests()
