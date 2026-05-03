# Task#3
# Program for list of 10 random num (ranging from 0 - 1000) and their sum using recursion

import random

num = [random.randint(1,1000) for i in range(10)]

print("10 randomly generated numbers (0-1000):", num)


def sum(n):
    if len(n) == 0:
        return 0
    else:
        return n[0] + sum(n[1:])

print("Sum of these numbers: ",(sum(n= num)))


