#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [bool(num) if num %
                2 == 0 else False for num in range(len(my_list))]
    return new_list
