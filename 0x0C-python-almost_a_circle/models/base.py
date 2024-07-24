#!/usr/bin/python3
"""The base module"""


class Base():
    """Class to keep track of other classes and objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the id attribute if defined"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
