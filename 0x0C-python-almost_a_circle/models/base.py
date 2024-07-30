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
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string representation of list_objs to a file

        Args:
            list_objs (list): List of instances that inherit from Base
        """
        filename = f"{cls.__name__}.json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dict))
        return filename

    @staticmethod
    def from_json_string(json_string):
        """A method that coverts a JSON string representation to a python List"""
        if json_string is not None:
            file_list = json.loads(json_string)
            return file_list
        return []
