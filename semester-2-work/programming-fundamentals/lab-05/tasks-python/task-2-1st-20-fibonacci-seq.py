# Task#2
# Recursive function for Fibonacci Sequence (1st 20 Terms)

def fibonacci(n):
    if n<=1:  # Base Case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print 1^st 20 terms
print("Fibonacci sequence:")

for i in range(20):
    print(fibonacci(i), end=" ")

