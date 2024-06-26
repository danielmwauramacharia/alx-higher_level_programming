#!/usr/bin/python3
"""Module that loads a JSON object to a python object"""
import json


def from_json_string(my_obj):
    """A function that loads a JSON object to python object"""
    my_obj = json.loads(my_obj)
    return my_obj
