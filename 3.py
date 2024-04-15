#!/usr/bin/env python3

# <p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
# <p>What is the largest prime factor of the number $600851475143$?</p>


def prime_factors(n):
    i = 2
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n = n // i
    print(n)


prime_factors(600851475143)

# 6857
