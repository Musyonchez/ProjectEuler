#!/usr/bin/env python3


# <p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
# <p>What is the largest prime factor of the number $600851475143$?</p>

"""
This module contains a function to find the largest prime factor of a given number.
It is a solution to the third problem from Project Euler.
"""


def prime_factors(n):
    """
    Finds and returns the largest prime factor of a given number.

    Parameters:
    n (int): The number to find the largest prime factor of.

    Returns:
    int: The largest prime factor of the given number.
    """
    i = 2
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n = n // i
    return n


print(prime_factors(600851475143))

# 6857
