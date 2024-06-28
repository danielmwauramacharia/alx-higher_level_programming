#!/usr/bin/python3
"""
Module: add_item

This module provides functionality to add command-line arguments to a list
stored in a JSON file. It allows users to accumulate a list of items incrementally
through multiple invocations of the script. The list is saved to and loaded from
a JSON file named 'add_item.json'.

Usage:
    ./add_item.py item1 item2 item3

Dependencies:
    - Python 3.x
    - json module (standard library)
    - sys module (standard library)
    - 6-load_from_json_file.py: Provides the function load_from_json_file
    - 5-save_to_json_file.py: Provides the function save_to_json_file

Functions:
    load_from_json_file(filename): Loads and returns a list from a JSON file.
    save_to_json_file(my_list, filename): Saves a list to a JSON file.

Error Handling:
    The script handles JSON decoding errors by initializing an empty list if the
    JSON file is empty or does not exist.
"""

import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    argList = load_from_json_file(filename)
except json.JSONDecodeError:
    argList = []
if len(sys.argv) > 1:
    sysList = sys.argv[1:]
    for item in sysList:
        argList.append(item)
save_to_json_file(argList, filename)
