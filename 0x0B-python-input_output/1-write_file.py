#!/usr/bin/python3
"""modeule that writes data to a file"""


def write_file(filename="", text=""):
    """A function that writes text to a file"""
    with open(filename, mode="w", encoding="utf-8") as objFile:
        count = objFile.write(text)
    return count
