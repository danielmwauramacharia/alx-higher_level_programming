#!/usr/bin/python3
def magic_string():
    magic_string.iter = getattr(magic_string, "iter", 0) + 1
    return ("BestSchool, " * (magic_string.iter - 1) + "BestSchool")
