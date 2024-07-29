#!/usr/bin/python3
"""Square module and inherits from Rectangle class"""
from models.rectangle import Rectangle
# Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """A class that defines the properties of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """The class constructor: gets attributes from the class Rectangle"""
        super().__init__(size, size, x=0, y=0, id=None)
        self.size = size
        self.x = x
        self.y = y
        # self.id = id

    def __str__(self):
        """Override method to print the details of the Square

        Returns:
            str: The string representation of the Square.
        """
        str_rep = ""
        name = type(self).__name__
        id_ = str(self.id)
        x = str(self.x)
        y = str(self.y)
        width_ = str(self.size)
        str_rep += "[" + name + "]" + " " + \
            "(" + id_ + ")" + " " + x + "/" + y + \
            " " + "-" + " " + width_
        return str_rep.strip()
