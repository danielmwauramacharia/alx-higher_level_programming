#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for item in matrix:
        for x in item:
            print("{:d} ".format(x), end='')
        print()
