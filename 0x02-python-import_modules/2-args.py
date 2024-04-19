#!/usr/bin/python3
import sys
length = len(sys.argv) - 1
if __name__ == "__main__":
    if length == 0:
        print("{} argument.".format(length))
    if length == 1:
        print("{} argument:".format(length))
    elif length > 1:
        print("{} arguments:".format(length))
    for i in range(length+1):
        if i == 0:
            continue
        print("{}{} {}".format(i, ":", sys.argv[i]))
