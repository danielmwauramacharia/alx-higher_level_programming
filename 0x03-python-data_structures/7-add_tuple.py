#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > len(tuple_b):
        result = list(tuple_a)
        shorter = tuple_b
    else:
        result = list(tuple_b)
        shorter = tuple_a
    for x, value in enumerate(shorter):
        result[x] += value
    final = result[0:2]
    return tuple(final)
