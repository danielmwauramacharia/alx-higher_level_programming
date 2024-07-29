#!/usr/bin/python3
"""The base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return []
