#!/usr/bin/env python3

# <p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
# <p>Find the sum of all the primes below two million.</p>

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))

def sum_of_primes(n):
    total = sum(i for i in range(2, n) if is_prime(i))
    print(total)

sum_of_primes(2000000)

# 142913828922
