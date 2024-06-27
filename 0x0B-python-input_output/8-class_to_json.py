#!/usr/bin/python3
"""Module that returns an object for serialization"""


def class_to_json(obj):
    """"
    Function that returns a simple object
    The object can be serialized to json

    """
    data = vars(obj)
    return data
