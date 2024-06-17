"""working with lists"""


class MyList(list):
    """inherits from list"""

    def __init__(self):
        """Instantiate a list object"""
        list.__init__(self)

    def print_sorted(self):
        """sorted list object in ascending order"""
        print(sorted(self))

    def __str__(self):
        """string rep of the object"""
        return list.__str__(self)
