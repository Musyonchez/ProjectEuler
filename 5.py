#!/usr/bin/env python3

# <p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
# <p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>


def smallest_multiple(n):
    i = n
    while True:
        for j in range(1, n + 1):
            if i % j != 0:
                break
        else:
            print(i)
            break
        i += n


smallest_multiple(20)
