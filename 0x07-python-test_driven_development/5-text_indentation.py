#!/usr/bin/python3
""""Working with Square"""


def print_square(size=0):
    """Print Square using # for the given Size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        for _ in range(size):
            print("#", end='')
        print()
