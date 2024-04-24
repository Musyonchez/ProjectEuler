# #!/usr/bin/env python3

# <p>If the numbers $1$ to $5$ are written out in words: one, two, three, four, five,
# then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.</p>
# <p>If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out
# in words, how many letters would be used? </p>
# <br><p class="note"><b>NOTE:</b> Do not count spaces or hyphens. For example, $342$
#  (three hundred and forty-two) contains $23$ letters and $115$ (one hundred and fifteen)
# contains $20$ letters. The use of "and" when writing out
# numbers is in compliance with British usage.</p>

"""
This module contains the solution to problem 17 from Project Euler.
It calculates the total number of letters used when all numbers
from 1 to 1000 are written out in words.
"""


def number_to_words(n):
    """
    Converts a number to its word representation.

    Args:
        n (int): The number to convert.

    Returns:
        str: The word representation of the number.
    """
    # Dictionary to map numbers to their word representations
    num_words = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "thousand",
    }

    if n == 1000:
        return "onethousand"

    words = ""
    if n >= 100:
        words += num_words[n // 100] + num_words[100]  # Add the hundreds place
        n %= 100
        if n > 0:
            words += "and"  # Add 'and' if there are additional digits

    if n > 0:
        if n <= 20:
            words += num_words[
                n
            ]  # Add the number directly for values less than or equal to 20
        else:
            words += num_words[(n // 10) * 10]  # Add the tens place
            n %= 10
            if n > 0:
                words += num_words[n]  # Add the ones place

    return words


TOTAL_LETTERS = 0
for i in range(1, 1001):
    word_representation = number_to_words(i)
    TOTAL_LETTERS += len(word_representation)

print("Total number of letters used:", TOTAL_LETTERS)


# letters = {
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
#     10: "ten",
#     11: "eleven",
#     12: "twelve",
#     13: "thirteen",
#     14: "fourteen",
#     15: "fifteen",
#     16: "sixteen",
#     17: "seventeen",
#     18: "eighteen",
#     19: "nineteen",
#     20: "twenty",
#     30: "thirty",
#     40: "forty",
#     50: "fifty",
#     60: "sixty",
#     70: "seventy",
#     80: "eighty",
#     90: "ninety",
#     100: "hundred",
#     1000: "thousand",
#     "and": "and",
# }


# # def get_number_letters(n):
# #     for _ in range(1, n):
# #         strn = str(n)
# #         if len(strn) <= 1:
# #             return get_number_letters_1(n)
# #         if len(strn) <= 2:
# #             return get_number_letters_2(n)
# #         if len(strn) <= 3:
# #             return get_number_letters_3(n)
# #         if len(strn) <= 4:
# #             return len(letters[1000])


# def get_number_letters(n):
#     total = 0
#     for a in range(1, n+1):
#         strn = str(a)
#         print(total)
#         if len(strn) <= 1:
#             total += get_number_letters_1(a)
#         elif len(strn) <= 2:
#             total += get_number_letters_2(a)
#         elif len(strn) <= 3:
#             total += get_number_letters_3(a)
#         elif len(strn) <= 4:
#             print(letters[1000])
#             total += len(letters[1000])


# def get_number_letters_1(n):
#     print(letters[n])
#     return len(letters[n])


# def get_number_letters_2(n):
#     if n in letters:
#         print(letters[n])
#         return len(letters[n])

#     digits = [int(d) for d in str(n)]

#     constr = f"{str(digits[0])}0"
#     first_digit = len(letters[int(constr)])
#     second_digit = len(letters[digits[1]])  # This will be 3

#     print(letters[int(constr)], letters[digits[1]])
#     return first_digit + second_digit


# def get_number_letters_3(n):
#     if n in letters:
#         print(letters[n])
#         return len(letters[n])

#     digits = [int(d) for d in str(n)]
#     constr = f"{str(digits[1])}0"
#     conint = int(constr)

#     first_digit = len(letters[digits[0]])
#     first_compound = len(letters[100])
#     if int(str(digits[1]) + str(digits[2])) in letters:
#         second_digit = len(letters[int(str(digits[1]) + str(digits[2]))])
#     else:
#         second_digit = len(letters[conint]) if digits[1] != 0 else 0
#     third_digit = len(letters[digits[2]]) if digits[2] != 0 else 0
#     and_word = len(letters["and"]) if digits[1] and digits[2] != 0 else 0

#     print(
#         letters[digits[0]],
#         letters[100],
#         letters["and"],
#         letters[conint] if digits[1] != 0 else 0,
#         letters[digits[2]] if digits[2] != 0 else 0,
#     )
#     # print(first_digit, first_compound, second_digit, and_word, third_digit)
#     return first_digit + first_compound + second_digit + and_word + third_digit


# print(get_number_letters(200))
