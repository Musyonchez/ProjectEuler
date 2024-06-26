#!/usr/bin/env python3

# <p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
# <p>Find the sum of all the primes below two million.</p>

"""
This module contains the solution to the tenth Project Euler problem.
It calculates the sum of all primes below two million.
"""


def is_prime(n):
    """
    Check if a number is prime.

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


def sum_of_primes(n):
    """
    Calculate the sum of all primes below a given number.

    Parameters:
    n (int): The upper limit for the primes.

    Returns:
    int: The sum of all primes below the given number.
    """
    total = sum(i for i in range(2, n) if is_prime(i))
    print(total)


sum_of_primes(2000000)

# 142913828922
