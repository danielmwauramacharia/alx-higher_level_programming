#!/usr/bin/python3
"""same kind"""


def inherits_from(obj, a_class):
    """checks if an object is a instance of a class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
