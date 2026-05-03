# Task #4
# Calculating Power of a num through Recursive Function


def power(base, exp):
    if exp == 0:   # base case
        return 1
    return base * power(base, exp - 1)         # base^exp = base × base^(exp−1)

# Taking Input
num = int(input("Enter the number: "))
pow = int(input("Enter the power: "))

# Calculating Result
result = power(num, pow)

# Result
print("Result: ", result)

