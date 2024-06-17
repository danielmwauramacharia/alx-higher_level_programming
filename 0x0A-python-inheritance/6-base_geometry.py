#!/usr/bin/python3
"""geometry module"""


class BaseGeometry():
    """Defining properties of a geometry"""

    def area(self):
        raise Exception("area() is not implemented")
