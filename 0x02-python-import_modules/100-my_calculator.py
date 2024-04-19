#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
length = len(sys.argv)
a = int(sys.argv[1])
b = int(sys.argv[3])
if length != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if sys.argv[2] == '+':
    print("{} + {} = {}".format(a, b, add(a, b)))
    sys.exit(0)
elif sys.argv[2] == '-':
    print("{} - {} = {}".format(a, b, sub(a, b)))
    sys.exit(0)
elif sys.argv[2] == '*':
    print("{} * {} = {}".format(a, b, mul(a, b)))
    sys.exit(0)
elif sys.argv[2] == '/':
    print("{} / {} = {}".format(a, b, div(a, b)))
    sys.exit(0)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
