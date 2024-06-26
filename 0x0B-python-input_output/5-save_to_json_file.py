#!/usr/bin/python3
"""Module that write an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object to a text file

    Using json representation.
    """
    jsonObject = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as fileObj:
        json.dump(my_obj, fileObj)
    return filename
