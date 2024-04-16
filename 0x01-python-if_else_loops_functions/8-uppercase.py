#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for i in str:
        y = ord(i)
        if y >= 97 and y <= 122:
            str = chr(y - 32)
            str1 += str
        else:
            str = chr(y)
            str1 += str
    print("{}\n".format(str1), end='')
