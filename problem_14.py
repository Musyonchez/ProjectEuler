#!/usr/bin/env python3

# <p>The following iterative sequence is defined for the set of positive integers:</p>
# <ul style="list-style-type:none;">
# <li>$n \to n/2$ ($n$ is even)</li>
# <li>$n \to 3n + 1$ ($n$ is odd)</li></ul>
# <p>Using the rule above and starting with $13$, we generate the following sequence:
# $$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$</p>

# <p>It can be seen that this sequence (starting at $13$ and finishing at $1$)
# contains $10$ terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at $1$.</p>

# <p>Which starting number, under one million, produces the longest chain?</p>

# <p class="note"><b>NOTE:</b> Once the chain starts the terms are
#  allowed to go above one million.</p>


"""
This module contains the solution to the fourteenth Project Euler problem.
It calculates the starting number, under one million, that produces the
 longest chain in the Collatz sequence.
"""


def collatz(n):
    """
    Calculate the Collatz sequence for a given number.

    Parameters:
    n (int): The starting number for the Collatz sequence.

    Returns:
    int: The length of the Collatz sequence starting from n.
    """
    count = 1
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    return count


MAX_CHAIN = 0

for i in range(1, 1000000):
    CHAIN = collatz(i)

    if CHAIN > MAX_CHAIN:
        MAX_CHAIN = CHAIN
        MAX_I = i

print(MAX_I)

# 837799
