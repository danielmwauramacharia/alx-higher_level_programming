#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("{}".format(matrix))
    for i in range(len(matrix)):
        new_list = [num for num in matrix[i]]
        for x, n in enumerate(new_list):
            if x != (len(new_list) - 1):
                print("{:d} ".format(n), end='')
            else:
                print("{:d}".format(n))
        del new_list
