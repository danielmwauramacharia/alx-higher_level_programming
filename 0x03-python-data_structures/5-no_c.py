#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    filtered = [l for l in my_list if l.lower() != 'c']
    my_string = ''.join(filtered)
    return my_string
