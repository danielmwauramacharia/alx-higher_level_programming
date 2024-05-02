#!/usr/bin/python3
import sys


class RaiseError(Exception):
    pass


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
        if not result:
            raise RaiseError
        return result
    except Exception as ex:
        message = "Exception: "
        sys.stderr.write("{}{}\n".format(message, ex))
        return None
