"""Sum of two numbers"""


def add_integer(a, b=98):
    """A function that returns sum of two numbers"""
    if a != a or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b != b or not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
