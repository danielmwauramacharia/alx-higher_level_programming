#!/usr/bin/python3
"""working with shape Rectangle"""


class Rectangle:
    """Defines properties of a rectangle"""

    def __init__(self, width=0, height=0):
        """Creating the rectangle object"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return thr contolled width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the acceptable value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return thr contolled height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the acceptable value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
