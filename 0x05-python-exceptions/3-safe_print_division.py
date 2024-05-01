#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return "{:.1f}".format(result)
    except ZeroDivisionError:
        return None
    finally:
        try:
            message = "Inside result: "
            print("{}{:.1f}".format(message, a / b))
        except ZeroDivisionError:
            print("{}{}".format(message, None))
