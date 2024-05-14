#!/usr/bin/python3
"""Working with a list of lists(matrix)"""


def matrix_divided(matrix, div):
    """A function that takes a matrix and devide it by div"""
    for item in matrix:
        # if item != item:
        #     raise TypeError(
        #         "matrix must be a matrix (list of lists) of integers/floats")

        for value in item:
            if value != value or not isinstance(value, (float, int)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    for _, items in enumerate(matrix):
        if len(matrix[0]) != len(items):
            raise TypeError("Each row of the matrix must have the same size")

    if div != div or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for items in matrix:
        helper_list = []
        for values in items:
            new_value = round(values/div, 2)
            helper_list.append(new_value)
        new_matrix.append(helper_list)
    return new_matrix
