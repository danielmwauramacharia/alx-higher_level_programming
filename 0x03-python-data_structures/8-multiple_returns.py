#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    tuple_mult = (length, None if length == 0 else sentence[0])
    return tuple_mult
