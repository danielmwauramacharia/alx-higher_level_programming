##!/usr/bin/python3
"""Square module and inherits from Rectangle class"""
# from models.rectangle import Rectangle
Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """A class that defines the properties of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """The class constructor: gets attributes from the class Rectangle"""
        # self.size = size
        # self.x = x
        # self.y = y
        # self.id = id
        super().__init__(size, size, x, y, id)

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

    @property
    def size(self):
        """Return the controlled value of size

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setting the size of the square

        Args:
            value (int): The size to be set.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes using non keyword values and keyworded values

        Args:
            *args: Non-keyword arguments to update attributes.
            **kwargs: Keyword arguments to update attributes by name.
        """
        if args is not None and len(args) != 0:
            attributes = ["id", "size", "x", "y"]
            c_attr = list(args)
            length = len(c_attr)
            length = min(length, 5)
            for i in range(length):
                setattr(self, attributes[i], c_attr[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
