#!/usr/bin/python3
"""geometry module"""


class BaseGeometry():
    """Defining properties of a geometry"""

    def area(self):
        """calculates are of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
