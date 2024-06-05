#!/usr/bin/python3
"""Working with matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """A function that multiplies two matrices using numpy"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(item, list) for item in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(item, list) for item in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or all(len(sublist) == 0 for sublist in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(sublist_) == 0 for sublist_ in m_b):
        raise ValueError("m_b can't be empty")
    if not all(all(isinstance(item, (int, float))
                   for item in sblist) for sblist in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(items, (int, float))
                   for items in sb_list) for sb_list in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if len({len(items) for items in m_a}) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len({len(items) for items in m_b}) > 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    np_a = np.array(m_a)
    np_b = np.array(m_b)
    matrix_result = np.dot(np_a, np_b)
    return matrix_result
