#!/usr/bin/python3
import sys


class RaiseError(Exception):
    pass


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
        if result is None and len(args) != 0:
            raise RaiseError
        return result
    except Exception as ex:
        message = "Exception: "
        sys.stderr.write("{}{}\n".format(message, ex))
        return None
