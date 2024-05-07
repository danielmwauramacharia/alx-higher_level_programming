#!/usr/bin/python3
"""Defining a Square"""


class Square:
    """Defining properties of a Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of Instance attributes """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the controlled size"""
        return self.__position

    @position.setter
    def position(self, value):
        """The controls for the size"""
        if not (isinstance(value, tuple) and len(value) == 2 and all(isinstance(x, int) for x in value) and all(y >= 0 for y in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the Square"""
        return self.__size * self.__size

    def my_print(self):
        """Print a square using #"""
        for i in range(self.__position[1]):
            print()
        if self.__size > 0:
            for i in range(self.__size):
                for value in range(self.__position[0]):
                    print(" ", end='')
                for x in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
