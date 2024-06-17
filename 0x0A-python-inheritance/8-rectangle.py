#!/usr.bin/bash
"""defining a rectangle"""


class Rectangle(BaseGeometry):
    """Geometry: Rectangle"""

    def __init__(self, width, height):
        """Instantiation"""
        if self.integer_validator("width", width) is True:
            self.__width = width
        if self.integer_validator("height", height) is True:
            self.__height = height
