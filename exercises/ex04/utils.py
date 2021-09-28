"""List utility functions."""

__author__ = "730444252"


# TODO: Implement your functions here.
def all(a: list[int], b: int) -> bool:
    """Check all."""
    if len(a) == 0:
        return False
    i: int = 0
    while i < len(a):
        if a[i] != b:
            return False
        else:
            i = i + 1
    return True 


def is_equal(a: list[int], b: list[int]) -> bool:
    """Check if two lists are equal."""
    i: int = 0
    if len(a) != len(b):
        return False
    while i < len(a):
        if a[i] != b[i]:
            return False
        else:
            i = i + 1
    return True


def max(a: list[int]) -> int:
    """Find the maximum."""
    if len(a) == 0:
        raise ValueError("max() arg is an empth List")
    i: int = 1
    biggest: int 
    while i < len(a):
        if a[0] < a[i]:
            a[0] = a[i]
            i = i + 1
        else:
            i = i + 1
    return a[0]
