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
        if isinstance(attr, list):
            if len(attr) == 0:
                return {}
            data_copy = dict(data)
            data_list = {}
            for item in attr:
                for key, value in data_copy.items():
                    if key == item:
                        data_list.update({key: value})
            return data_list
        return data

    def reload_from_json(self, json):
        """
        Json containind student attributes
        Those attributes creates a new student object
        """
        data = vars(self)
        dataList = []
        for key in data.keys():
            dataList.append(key)
        for _, x in enumerate(dataList):
            for kiy, val in json.items():
                if hasattr(self, x):
                    delattr(self, x)
                    setattr(self, kiy, val)
                else:
                    continue
        return self
