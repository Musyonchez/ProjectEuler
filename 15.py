#!/usr/bin/env python3

# <p>Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.</p>
# <div class="center">
# <img src="resources/images/0015.png?1678992052" class="dark_img" alt=""></div>
# <p>How many such routes are there through a $20 \times 20$ grid?</p>


def lattice_paths(n):
    
    paths = 1
    for i in range(n):
        paths *= 2 * n - i
        paths //= i + 1
    return paths


print(lattice_paths(20))

# 137846528820
