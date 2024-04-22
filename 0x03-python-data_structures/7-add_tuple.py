##!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return (0, 0)
    if len(tuple_a) > len(tuple_b):
        result = list(tuple_a)
        shorter = tuple_b
    elif len(tuple_b) > len(tuple_a):
        result = list(tuple_b)
        shorter = tuple_a
    else:
        if len(tuple_a) == 1 and len(tuple_b) == 1:
            result = list(tuple_a)
            result.append(0)
            shorter = tuple_b
        else:
            result = list(tuple_a)
            shorter = tuple_b
    for x, value in enumerate(shorter):
        result[x] += value
    final = result[0:2]
    return tuple(final)
