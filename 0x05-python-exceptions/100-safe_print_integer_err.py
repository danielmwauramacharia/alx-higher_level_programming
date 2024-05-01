#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as ex:
        message = "Exception: "
        sys.stderr.write("{0}{1}\n".format(message, ex))
        return False
