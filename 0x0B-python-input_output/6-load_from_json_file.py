#!/usr/bin/python3
"""Module that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return json.load(f)
    #     pyObject = json.loads(f)
    # return pyObject


filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))
