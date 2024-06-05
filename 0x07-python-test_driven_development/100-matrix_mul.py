#!/usr/bin/python3
"""Working with matrices"""


def matrix_mul(m_a, m_b):
    """A function that multiplies two matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_a, list):
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
    matrix_result = []
    for _, row in enumerate(m_a):
        helper_matrix = []
        for j in range(len(m_b[0])):
            sum_ = 0
            for k, val in enumerate(row):
                sum_ += val * m_b[k][j]
            helper_matrix.append(sum_)
        matrix_result.append(helper_matrix)
    return matrix_result
