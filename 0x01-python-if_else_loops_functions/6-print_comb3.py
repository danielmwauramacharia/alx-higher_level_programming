#!/usr/bin/python3
x = 0
for i in range(10):
    for n in range(x, 10):
        if i == n:
            continue
        if i < 8:
            print("{}{}, ".format(i, n), end='')
        else:
            print("{}{}{}".format(i, n, "\n"), end='')
    x += 1
