#!/usr/bin/python3
"""working with shape Rectangle"""


class Rectangle:
    """Defines properties of a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Creating the rectangle object"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return thr contolled width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the acceptable value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return thr contolled height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the acceptable value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectagle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of our object"""
        rect = ""
        symbol = str(self.print_symbol)
        if self.height != 0 or self.width != 0:
            for _ in range(self.height):
                rect += symbol * self.width + "\n"
        return rect.strip()

    def __repr__(self):
        """String representation of rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Called when an object is about to be deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
