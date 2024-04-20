#!/usr/bin/env python3

# <p>A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
# $$a^2 + b^2 = c^2.$$</p>
# <p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
# <p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p>

def pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
            
print(pythagorean_triplet(1000))

# 31875000