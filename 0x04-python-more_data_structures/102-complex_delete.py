#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            key_list.append(key)
    for item in key_list:
        del a_dictionary[item]
    return a_dictionary
