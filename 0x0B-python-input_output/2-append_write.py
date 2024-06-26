#!/usr/bin/python3
"""modeule that append text to a file"""


def append_write(filename="", text=""):
    """A function that writes text to a file"""
    with open(filename, mode="a", encoding="utf-8") as objFile:
        count = objFile.write(text)
    return count
