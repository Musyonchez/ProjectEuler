#!/usr/bin/env python3

# <p>The sequence of triangle numbers is generated by
#  adding the natural numbers. So the $7$<sup>th</sup>
#  triangle number would be $1 + 2 + 3 + 4 + 5 + 6 + 7 = 28$.
#  The first ten terms would be:
# $$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, \dots$$</p>
# <p>Let us list the factors of the first seven triangle numbers:</p>
# \begin{align}
# \mathbf 1 &amp;\colon 1\\
# \mathbf 3 &amp;\colon 1,3\\
# \mathbf 6 &amp;\colon 1,2,3,6\\
# \mathbf{10} &amp;\colon 1,2,5,10\\
# \mathbf{15} &amp;\colon 1,3,5,15\\
# \mathbf{21} &amp;\colon 1,3,7,21\\
# \mathbf{28} &amp;\colon 1,2,4,7,14,28
# \end{align}
# <p>We can see that $28$ is the first triangle number to have over five divisors.</p>
# <p>What is the value of the first triangle number to have over five hundred divisors?</p>


#!/usr/bin/env python3

"""
This module contains the solution to the twelfth Project Euler problem.
It calculates the value of the first triangle number to have over five hundred divisors.
"""


def triangle_number(num):
    """
    Calculate the nth triangle number.

    Parameters:
    num (int): The position of the triangle number.

    Returns:
    int: The nth triangle number.
    """
    return num * (num + 1) // 2


def divisors(num):
    """
    Calculate the number of divisors of a number.

    Parameters:
    num (int): The number to find the divisors of.

    Returns:
    int: The number of divisors of the given number.
    """
    return sum(2 for i in range(1, int(num**0.5) + 1) if num % i == 0)


N = 1

while True:
    if divisors(triangle_number(N)) > 500:
        print(triangle_number(N))
        break
    N += 1
# 76576500
