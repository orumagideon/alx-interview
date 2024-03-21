#!/usr/bin/python3
""" Provided a number
n, write a method that calculates the fewest number
of operations needed to result in exactly n H
characters in the file."""


def minOperations(n: int) -> int:
    """function calculates the fewest number of operations
    needed to result in exactly n H characters"""
    process = 2
    op = 0
    while n > 1:
        while n % process == 0:
            op += process
            n /= process
        process += 1
    return op
