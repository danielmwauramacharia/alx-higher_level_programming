#!/usr/bin/python3
"""working with shape Rectangle"""


class Rectangle:
    """Defines properties of a rectangle"""

    def __init__(self, width=0, height=0):
        """Creating the rectangle object"""
        self.width = width
        self.height = height

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

    def area(self):
        """Calculates the area of a rectagle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of our object"""
        rect = ""
        if self.height != 0 or self.width != 0:
            for _ in range(self.height):
                rect += "#" * self.width + '\n'
        return rect.strip()
