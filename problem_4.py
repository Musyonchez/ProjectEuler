#!/usr/bin/env python3

# <p>A palindromic number reads the same both ways. The largest
#  palindrome made from the product of two $2$-digit
#  numbers is $9009 = 91 \times 99$.</p>
# <p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>

"""
This module contains functions to find the largest palindrome made
 from the product of two 3-digit numbers.
It is a solution to the fourth problem from Project Euler.
"""

import itertools


def is_palindrome(n):
    """
    Checks if a number is a palindrome.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    return str(n) == str(n)[::-1]


def largest_palindrome():
    """
    Finds and returns the largest palindrome made from the product of two 3-digit numbers.

    Returns:
    int: The largest palindrome made from the product of two 3-digit numbers.
    """
    largest = 0
    for i, j in itertools.product(range(100, 1000), range(100, 1000)):
        product = i * j
        if is_palindrome(product) and product > largest:
            largest = product
    return largest


print(largest_palindrome())

# 906609
