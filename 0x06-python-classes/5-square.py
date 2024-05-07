#!/usr/bin/python3
"""Defining a Square"""


class Square:
    """Defining properties of a Square
    """

    def __init__(self, size=0):
        """Initialization of Instance attributes """
        self.__size = size

    @property
    def size(self):
        """Return the controlled size"""
        return self.__size

    @size.setter
    def size(self, value):
        """The controls for the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the Square"""
        return self.__size * self.__size

    def my_print(self):
        """Print a square using #"""
        if self.__size > 0:
            for i in range(self.__size):
                for x in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()

