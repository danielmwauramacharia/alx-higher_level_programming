#!/usr/bin/python3
"""modeule that writes data to a file"""


def write_file(filename="", text=""):
    """A function that writes text to a file"""
    with open(filename, mode="w", encoding="utf-8"):
        filename.write(text)
        count = 0
        for words in filename:
            for _ in words:
                count += 1
        return count
