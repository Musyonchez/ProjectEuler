#!/usr/bin/env python3

# <p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
# <p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>

total = 0


def sum(count):
    for i in range(1, count):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i


print(total)

sum(1000)
