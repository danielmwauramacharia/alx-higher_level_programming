#!/usr/bin/python3

"""module defining the class rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defining class rectangle """

    def __init__(self, width, height):
        """instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Extend the functionality of method area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the class"""
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
