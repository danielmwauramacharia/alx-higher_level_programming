#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    lastDidit = number % 10
    return lastDidit
