#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing The functionality of our module max_integer.py """

    def test_empty(self):
        """Test for an empty list"""
        self.assertAlmostEqual(max_integer([]), None)

    def test_one_element(self):
        """Test for a list with one Element"""
        self.assertAlmostEqual(max_integer([4]), 4)

    def test_negative(self):
        """A list wit negative numbers"""
        neg_list = [-2, -1, -3, -4, -5]
        self.assertAlmostEqual(max_integer(neg_list), -1)

    def test_one_negative(self):
        """List with one negative number"""
        one_list = [2, 4, 5, 9, 6, -7]
        self.assertAlmostEqual(max_integer(one_list), 9)

    def test_end(self):
        """List with max at the end"""
        self.assertAlmostEqual(max_integer(list(range(5))), 4)

    def test_start(self):
        """List with the max at the beginning"""
        self.assertAlmostEqual(max_integer(list(reversed(range(6)))), 5)

    def test_middle(self):
        """List with max at the middle"""
        my_list = [1, 3, 5, 6, 4, 2, 0]
        self.assertAlmostEqual(max_integer(my_list), 6)
