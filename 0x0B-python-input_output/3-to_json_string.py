#!/usr/bin/python3
"""Module that dumps a string object"""
import json


def to_json_string(my_obj):
    """A function that dumps a string object to JSON"""
    my_obj = json.dumps(my_obj)
    return my_obj
