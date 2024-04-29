#!/usr/bin/python3
def weight_average(my_list):
    if not my_list:
        return 0
    sum_1 = sum(div for _, div in my_list)
    sum_2 = sum(x * y for x, y in my_list)
    if sum_1 == 0:
        return 0
    average = sum_2 / sum_1
    return average
