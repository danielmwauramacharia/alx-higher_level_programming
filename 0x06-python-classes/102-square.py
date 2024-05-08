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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the Square"""
        return self.__size**2

    def __eq__(self, other):
        """Method that checks the equality of objects.area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the Equality Operator"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Override the less than operator"""
        return self.area() < other.area()

    def __le__(self, other):
        """Override less than or Equal to operator"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """override greator than operator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override Greator than or equal to operators"""
        return self.area() >= other.area()
