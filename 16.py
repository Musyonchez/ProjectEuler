#!/usr/bin/env python3

# <p>$2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.</p>
# <p>What is the sum of the digits of the number $2^{1000}$?</p>


def power(n):
    sum = 2**n
    total = 0
    for d in str(sum):
        total = total + int(d)
    return total


print(power(1000))

# 1366
