#!/usr/bin/python3
""" 
Module that adds all arguments to a Python list,

and then save them to a file
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
