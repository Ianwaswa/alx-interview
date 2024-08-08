#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generates a list of lists representing Pascal's triangle up to level n.

    @param n: The number of levels of Pascal's triangle to generate.
    @return: A list of lists of integers representing Pascal's triangle.
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1  # The first value in each row is always 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j  # Calculate the next value in the row
            res.append(level)
    return res
