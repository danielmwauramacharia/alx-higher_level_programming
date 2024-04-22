#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    filtered = [letter for letter in my_list if letter.lower() != 'c']
    my_string = ''.join(filtered)
    return my_string
