#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastdigit = number % 10
    print(f"Last digit of {number} is {lastdigit} ", end='')
    if lastdigit > 5:
        print("and is greater than 5")
    elif 0 < lastdigit < 6:
        print("and is less than 6 and not 0")
    else:
        print("and is 0")
else:
    lastdigit = -1 * (abs(number) % 10)
    print(f"Last digit of {number} is {lastdigit} ", end='')
    if lastdigit != 0:
        print("and is less than 6 and not 0")
    else:
        print("and is 0")
