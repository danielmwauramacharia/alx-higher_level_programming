#!/usr/bin/python3
"""Module that write an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object to a text file

    Using json representation.
    """
    if isinstance(my_obj, set):
        my_obj = list(my_obj)
    jsonObject = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as fileObj:
        fileObj.write(jsonObject)
    return filename
