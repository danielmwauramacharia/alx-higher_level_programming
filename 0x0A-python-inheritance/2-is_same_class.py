#!/usr/bin/python3
"""same object"""


def is_same_class(obj, a_class):
    """checks if object belongs to a class"""
    if isinstance(obj, a_class) and a_class != object:
        return True
    else:
        return False
