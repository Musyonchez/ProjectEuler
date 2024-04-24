#!/usr/bin/env python3

# <p>The sum of the squares of the first ten natural numbers is,</p>
# $$1^2 + 2^2 + ... + 10^2 = 385.$$
# <p>The square of the sum of the first ten natural numbers is,</p>
# $$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
# <p>Hence the difference between the sum of the squares of the
#  first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
# <p>Find the difference between the sum of the squares of the
#  first one hundred natural numbers and the square of the sum.</p>

"""
This module contains functions to find the difference between
 the sum of the squares of the first one hundred natural numbers
 and the square of the sum.
It is a solution to the sixth problem from Project Euler.
"""


def sum_of_squares(n):
    """
    Calculates and returns the sum of the squares of the first n natural numbers.

    Parameters:
    n (int): The number of natural numbers to include in the calculation.

    Returns:
    int: The sum of the squares of the first n natural numbers.
    """
    return sum(i**2 for i in range(1, n + 1))


def square_of_sum(n):
    """
    Calculates and returns the square of the sum of the first n natural numbers.

    Parameters:
    n (int): The number of natural numbers to include in the calculation.

    Returns:
    int: The square of the sum of the first n natural numbers.
    """
    return sum(range(1, n + 1)) ** 2


print(square_of_sum(100) - sum_of_squares(100))

# 25164150
