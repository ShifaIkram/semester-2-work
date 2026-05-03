# TASK#1
# Calculation of Permutation and Combinations by Recursive Function
# Permutation = nPr = n!/(n-r)!
# Combination = nCr = n!/r!(n-r)!

# Not using in-built function for factorial (recursion)
def factorial(n):
    fact = 1   #bcs factorial multiplication starts from 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# For Permutation Calculation
def permutation(n, r):
    return factorial(n) // factorial(n - r)       # // = integer division (no decimal)

# For Combination Calculation
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Actual Calculations
# take input from the user
n = int(input("Enter n: "))
r = int(input("Enter r: "))

 # Calling Functions
print("Permutation (nPr) = ", permutation(n, r))
print("Combination (nCr) = ", combination(n, r))


