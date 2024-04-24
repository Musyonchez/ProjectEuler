#!/usr/bin/env python3

# <p>By listing the first six prime numbers: $2, 3, 5, 7, 11$,
#  and $13$, we can see that the $6$th prime is $13$.</p>
# <p>What is the $10\,001$st prime number?</p>
# .</p>

"""
This module contains functions to find the nth prime number.
It is a solution to the seventh problem from Project Euler.
"""


def is_prime_number(n):
    """
    Checks if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))


def nth_prime(n):
    """
    Finds and returns the nth prime number.

    Parameters:
    n (int): The position of the prime number to find.

    Returns:
    int: The nth prime number.
    """
    count = 1
    i = 1
    while count < n:
        i += 2
        if is_prime_number(i):
            count += 1
    return i


print(nth_prime(10001))

# 104743
