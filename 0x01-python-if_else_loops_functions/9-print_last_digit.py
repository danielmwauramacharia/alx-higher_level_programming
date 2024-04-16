#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    lastdigit = number % 10
    print("{}".format(lastdigit), end='')
    return lastdigit
