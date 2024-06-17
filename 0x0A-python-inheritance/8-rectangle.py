#!/usr/bin/python3
"""
Module that defines class rectangle based on class base geometry

Its part of geometry package
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class represent rectangle

    inherits the attributes and methods from class basegeometry
    """

    def __init__(self, width, height):
        """
        Instantiation of Rectangle with specified width and height

        args

        width(int): width of the rectangle
        height(int): height of the rectangle     
        """
        if self.integer_validator("width", width) is True:
            self.__width = width
        if self.integer_validator("height", height) is True:
            self.__height = height
