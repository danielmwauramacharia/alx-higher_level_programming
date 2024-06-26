#!/usr/bin/python3
"""Module that reads a file"""


def read_file(filename=""):
    """A function that displays a passed file in the stdout"""
    with open(filename, encoding="utf-8") as fileObj:
        print(fileObj.read())