#!/usr/bin/env python3

# <p>$2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.</p>
# <p>What is the sum of the digits of the number $2^{1000}$?</p>


"""
This module contains the solution to the sixteenth Project Euler problem.
It calculates the sum of the digits of the number 2^1000.
"""


def power(n):
    """
    Calculate the sum of the digits of 2 raised to the power of n.

    Parameters:
    n (int): The exponent to which 2 is raised.

    Returns:
    int: The sum of the digits of 2^n.
    """
    result = 2**n
    total = 0
    for d in str(result):
        total = total + int(d)
    return total


print(power(1000))

# 1366
