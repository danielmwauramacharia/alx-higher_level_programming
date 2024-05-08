#!/usr/bin/python3
"""A cricle and its properties: Area and Circumference"""
import math


class MagicClass:
    """A class defining a circle and its properties"""

    def __init__(self, radius=0):
        """Private Instance to set attribute raduius of a circle"""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates The area of a circle"""
        return math.pi * self.__radius**2

    def circumference(self):
        """Calculates the circumference of a circle"""
        return 2 * math.pi * self.__radius
