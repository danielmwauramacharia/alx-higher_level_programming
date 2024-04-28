#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_list = []
    for row in matrix:
        square_row = [item * item for item in row]
        square_list.append(square_row)
    return square_list
