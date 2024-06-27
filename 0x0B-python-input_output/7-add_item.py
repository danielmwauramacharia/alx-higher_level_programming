#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then save them to a file"""
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"
if os.path.exists(filename):
    argList = load_from_json_file(filename)
else:
    argList = []
if len(sys.argv) > 1:
    sysList = sys.argv[1:]
    for item in sysList:
        argList.append(sysList)
save_to_json_file(argList, filename)
