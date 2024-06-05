#!/usr/bin/python3
"""Working with matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """A function that multiplies two matrices using numpy"""
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not all(isinstance(item, list) for item in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(item, list) for item in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or all(len(sublist) == 0 for sublist in m_a):
        raise ValueError(
            f"shapes {np.shape(m_a)} and {np.shape(m_b)} not aligned: "
            f"{len(m_a[0])} (dim 1) != {len(m_b)} (dim 0)"
        )
    if len(m_b) == 0 or all(len(sublist_) == 0 for sublist_ in m_b):
        raise ValueError(
            f"shapes {np.shape(m_b)} and {np.shape(m_a)} not aligned: "
            f"{len(m_b[0])} (dim 1) != {len(m_a)} (dim 0)"
        )
    if not all(all(isinstance(item, (int, float))
                   for item in sblist) for sblist in m_a):
        raise TypeError("invalid data type for einsum")
    if not all(all(isinstance(items, (int, float))
                   for items in sb_list) for sb_list in m_b):
        raise TypeError("invalid data type for einsum")
    if len({len(items) for items in m_a}) > 1:
        raise TypeError("setting an array element with a sequence.")
    if len({len(items) for items in m_b}) > 1:
        raise TypeError("setting an array element with a sequence.")
    rows_a, cols_a = np.shape(m_a)
    rows_b, cols_b = np.shape(m_b)
    if cols_a != rows_b:
        raise ValueError(
            f"shapes {rows_a,cols_a} and {rows_b,cols_b} not aligned: "
            f"{cols_a} (dim 1) != {rows_b} (dim 0)"
        )
    np_a = np.array(m_a)
    np_b = np.array(m_b)
    matrix_result = np.dot(np_a, np_b)
    return matrix_result
