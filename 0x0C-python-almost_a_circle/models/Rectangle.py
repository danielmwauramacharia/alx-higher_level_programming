#!/usr/bin/python3
"""Rectangle module"""
Base = __import__('base').Base


class Rectangle(Base):
    """Defining the properties of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The rectangle constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """Return the controlled value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value of width"""
        self.__width = value

    @property
    def height(self):
        """Return the controlled value of width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the value of width"""
        self.__height = value

    @property
    def x(self):
        """Return the controlled value of width"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the value of width"""
        self.__x = value

    @property
    def y(self):
        """Return the controlled value of width"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the value of width"""
        self.__y = value
