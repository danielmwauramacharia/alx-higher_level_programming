#!/usr/bin/python3
"""Rectangle module and inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Defining the properties of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The rectangle constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """Return the controlled value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the controlled value of width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the value of width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return the controlled value of width"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the value of width"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return the controlled value of width"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the value of width"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display the rectangle instance using #"""
        for _ in range(self.height):
            for _ in range(self.width):
                print("#", end="")
            print()
