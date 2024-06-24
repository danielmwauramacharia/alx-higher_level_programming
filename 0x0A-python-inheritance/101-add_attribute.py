#!/usr/bin/python3
"""Attributes to an object"""


def add_attribute(obj, name, value):
    """function creates attributes to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
