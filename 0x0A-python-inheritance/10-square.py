#!/usr/bin/python3

"""module defining the class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defining the properties of Square"""

    def __init__(self, size):
        """initialization of square sizes"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
