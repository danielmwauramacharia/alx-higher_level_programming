#!/usr/bin/python3
"""geometry module"""


class BaseGeometry():
    """Defining properties of a geometry"""

    def area(self):
        """calculates are of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value"""
        if not (isinstance(value, int) and type(value) is int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
