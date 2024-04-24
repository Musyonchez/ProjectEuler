#!/usr/bin/env python3

# <p>Starting in the top left corner of a $2 \times 2$ grid,
#  and only being able to move to the right and down, there
#  are exactly $6$ routes to the bottom right corner.</p>
# <div class="center">
# <img src="resources/images/0015.png?1678992052" class="dark_img" alt=""></div>
# <p>How many such routes are there through a $20 \times 20$ grid?</p>

"""
This module contains the solution to the fifteenth Project Euler problem.
It calculates the number of routes through a 20x20 grid, starting
 in the top left corner and only being able to move right and down.
"""


def lattice_paths(n):
    """
    Calculate the number of routes through a grid of size n x n,
     starting in the top left corner and only being able to move right and down.

    Parameters:
    n (int): The size of the grid.

    Returns:
    int: The number of routes through the grid.
    """
    paths = 1
    for i in range(n):
        paths *= 2 * n - i
        paths //= i + 1
    return paths


print(lattice_paths(20))

# 137846528820
