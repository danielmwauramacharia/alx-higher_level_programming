#!/usr/bin/python3
"""Rectangle module and inherits from Base class"""
from models.base import Base
# Base = __import__('base').Base


class Rectangle(Base):
    """Defining the properties of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The rectangle constructor

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y coordinate of the rectangle. Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """Return the controlled value of width

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the value of width

        Args:
            value (int): The width to be set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the controlled value of height

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the value of height

        Args:
            value (int): The height to be set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return the controlled value of x

        Returns:
            int: The x coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the value of x

        Args:
            value (int): The x coordinate to be set.

        Raises:
            TypeError: If the x coordinate is not an integer.
            ValueError: If the x coordinate is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return the controlled value of y

        Returns:
            int: The y coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the value of y

        Args:
            value (int): The y coordinate to be set.

        Raises:
            TypeError: If the y coordinate is not an integer.
            ValueError: If the y coordinate is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """Display the rectangle instance using #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Override method to print the details of the rectangle

        Returns:
            str: The string representation of the rectangle.
        """
        str_rep = ""
        name = type(self).__name__
        id_ = str(self.id)
        x = str(self.x)
        y = str(self.y)
        width_ = str(self.width)
        height_ = str(self.height)
        str_rep += "[" + name + "]" + " " + \
            "(" + id_ + ")" + " " + x + "/" + y + \
            " " + "-" + " " + width_ + "/" + height_
        return str_rep.strip()

    def update(self, *args, **kwargs):
        """Update the attributes using non keyword values and keyworded values

        Args:
            *args: Non-keyword arguments to update attributes in the order: id, width, height, x, y.
            **kwargs: Keyword arguments to update attributes by name.
        """
        if args is not None and len(args) != 0:
            attributes = ["id", "width", "height", "x", "y"]
            c_attr = list(args)
            length = len(c_attr)
            length = min(length, 5)
            for i in range(length):
                setattr(self, attributes[i], c_attr[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
