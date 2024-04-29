#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_1 = 0
    for item in my_list:
        div = list(item)[len(item)-1]
        sum_1 += div
    sum_2 = 0
    for item in my_list:
        result = 1
        for _, x in enumerate(item):
            result *= x
        sum_2 += result
    average = sum_2 / sum_1
    return average
