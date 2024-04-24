#!/usr/bin/env python3

# <p>A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
# $$a^2 + b^2 = c^2.$$</p>
# <p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
# <p>There exists exactly one Pythagorean triplet for which
#  $a + b + c = 1000$.<br>Find the product $abc$.</p>


"""
This module contains a solution to Project Euler problem 9.
It finds the product of a Pythagorean triplet for which a + b + c = 1000.
"""


def pythagorean_triplet(n):
    """
    Finds the product of a Pythagorean triplet for which a + b + c = n.

    Parameters:
    n (int): The sum of the triplet.

    Returns:
    int: The product of the Pythagorean triplet.
    """
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return None  # Ensure a consistent return statement


print(pythagorean_triplet(1000))

# 31875000
