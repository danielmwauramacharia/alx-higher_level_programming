#!/usr/bin/python3
"""module that creates a class and return attribute of an instance"""


class Student():
    """A class that contain the attributes of a student"""

    def __init__(self, first_name, last_name, age):
        """Initialization of the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """"Returns the attributes of an instance in a dict"""
        data = vars(self)
        data_copy = dict(data)
        if isinstance(attr, list):
            if len(attr) != 0:
                for item in attr:
                    for key in data_copy:
                        if key != item:
                            del data_copy[key]
                return data_copy
            return data
        return data
