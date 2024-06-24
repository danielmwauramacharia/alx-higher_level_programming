#!/usr/bin/python3
"""module dealing with integer"""


class MyInt(int):
    """class that inherits from int"""

    def __init__(self, integer):
        """Initialization"""
        self.integer = integer

    def __str__(self):
        """string representation of object"""
        return "{:d}".format(self.integer)

    def __eq__(self, integer):
        """Equality check"""
        return not (self.integer == integer)

    def __ne__(self, integer):
        """Non Equality check"""
        return not (self.integer != integer)
