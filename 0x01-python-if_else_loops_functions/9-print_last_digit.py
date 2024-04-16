#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    l = number % 10
    print("{}".format(l), end ='')
    return l
