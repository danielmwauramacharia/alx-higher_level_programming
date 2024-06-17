#!/usr/bin/python3
"""same kind"""


def is_kind_of_class(obj, a_class):
    """checks if an object is a instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
