#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    count = -1
    for i in str:
        count += 1
        if count == n:
            continue
        str1 += i
    return str1
