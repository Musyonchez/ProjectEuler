#!/usr/bin/env python3

# <p>$2520$ is the smallest number that can be divided by each of
#  the numbers from $1$ to $10$ without any remainder.</p>
# <p>What is the smallest positive number that is <strong
#  class="tooltip">evenly divisible<span class="tooltiptext">divisible
#  with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>

"""
This module contains a function to find the smallest positive number
 that is evenly divisible by all of the numbers from 1 to 20.
It is a solution to the fifth problem from Project Euler.
"""


def smallest_multiple(n):
    """
    Finds and returns the smallest positive number that is evenly
      divisible by all of the numbers from 1 to n.

    Parameters:
    n (int): The upper limit for the range of numbers to check divisibility against.

    Returns:
    int: The smallest positive number that is evenly divisible by
    all of the numbers from 1 to n.
    """
    i = n
    while True:
        for j in range(1, n + 1):
            if i % j != 0:
                break
        else:
            return i
        i += n


print(smallest_multiple(20))

# 232792560
