#!/usr/bin/python3
""" Module that add CL arguments to a list"""
import json
import sys
if __name__ == "__main__":
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"
    try:
        argList = load_from_json_file(filename)
    except (json.JSONDecodeError, FileNotFoundError):
        argList = []
    argList.extend(sys.argv[1:])
    save_to_json_file(argList, filename)
