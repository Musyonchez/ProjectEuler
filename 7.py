#!/usr/bin/env python3

# <p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.</p>
# <p>What is the $10\,001$st prime number?</p>
# .</p>


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))


def nth_prime(n):
    count = 1
    i = 1
    while count < n:
        i += 2
        if is_prime(i):
            count += 1
    print(i)


nth_prime(10001)

# 104743
