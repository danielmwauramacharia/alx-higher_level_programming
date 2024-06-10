#!/usr/bin/python3
"""No creating additional attributes"""


class LockedClass:
    """A class that have controlled attributes"""
    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        """Instantiation"""
        self.first_name = first_name
