#!/usr/bin/env python3

# <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
# <p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>

import itertools


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def largest_palindrome():
    largest = 0
    for i, j in itertools.product(range(100, 1000), range(100, 1000)):
        product = i * j
        if is_palindrome(product) and product > largest:
            largest = product
    print(largest)


largest_palindrome()
