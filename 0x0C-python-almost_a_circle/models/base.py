#!/usr/bin/python3
"""The base module"""
import json
import os


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
                list_str = cls.to_json_string(list_dict)
                file.write(list_str)

    @staticmethod
    def from_json_string(json_string):
        """A method that coverts a JSON string to a python list"""
        if json_string is not None:
            file_list = json.loads(json_string)
            return file_list
        return []

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance from already an existing one"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(12, 13)
        else:
            new_instance = cls(10)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """A JSON file that creates instances and return them as a list"""
        instances = []
        if os.path.exists(f"{cls.__name__}.json") \
                and os.path.getsize(f"{cls.__name__}.json") != 0:
            with open(f"{cls.__name__}.json", mode="r", encoding="utf8") \
                    as file:
                file_list = file.read()
            dict_list = cls.from_json_string(file_list)
            for dict_attr in dict_list:
                instance_created = cls.create(**dict_attr)
                instances.append(instance_created)
        return instances
