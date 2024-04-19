#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list_names = dir(hidden_4)
    b = 0
    for i in list_names:
        name = i
        if name[0] == '_' and name[1] == '_':
            continue
        print(name)
        b += 1
