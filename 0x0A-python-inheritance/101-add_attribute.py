#!/usr/bin/python3
"""module to add attribute"""


def add_attribute(obj, name, value):
    """function that adds attributes to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value
