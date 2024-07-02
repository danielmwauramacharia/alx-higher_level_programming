#!/usr/bin/python3
"""Module dealing with pascal triangle"""


def pascal_triangle(n):
    """A function that prints pascal triangle lists"""
    if n <= 0:
        return []
    triangle = []
    for _ in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend(sum(pair) for pair in zip(last_row, last_row[1:]))
            row.append(1)
        triangle.append(row)
    return triangle
