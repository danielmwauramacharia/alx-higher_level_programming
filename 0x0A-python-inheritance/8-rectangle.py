#!/usr/bin/python3

"""module defining the class rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defining class rectangle """

    def __init__(self, width, height):
        """instantiation"""
        if self.integer_validator("width", width) is True:
            self.__width = width
        if self.integer_validator("height", height) is True:
            self.__height = height
