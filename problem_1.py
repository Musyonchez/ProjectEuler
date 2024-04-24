#!/usr/bin/env python3

# <p>If we list all the natural numbers below $10$ that are
#  multiples of $3$ or $5$, we get $3, 5, 6$ and $9$.
#  The sum of these multiples is $23$.</p>
# <p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>


"""
This module contains the solution to the first Project Euler problem.
It calculates the sum of all multiples of 3 or 5 below 1000.
"""


def calculate_sum(count):
    """
    Calculate the sum of all multiples of 3 or 5 below the given count.

    Parameters:
    count (int): The upper limit for the multiples.

    Returns:
    int: The sum of all multiples of 3 or 5 below the count.
    """
    total = 0
    for i in range(1, count):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i
    return total


print(calculate_sum(1000))
# 233168
