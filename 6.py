#!/usr/bin/env python3

# <p>The sum of the squares of the first ten natural numbers is,</p>
# $$1^2 + 2^2 + ... + 10^2 = 385.$$
# <p>The square of the sum of the first ten natural numbers is,</p>
# $$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
# <p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
# <p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>


def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))


def square_of_sum(n):
    return sum(range(1, n + 1)) ** 2


print(square_of_sum(100) - sum_of_squares(100))

# 25164150
