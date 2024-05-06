#!/usr/bin/python3
"""Defining a Square"""


class Square:
    """Defining properties of a Square
    """

    def __init__(self, size):
        """Initialization of Instance attributes """
        try:
            if size is not int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except (TypeError, ValueError):
            pass
