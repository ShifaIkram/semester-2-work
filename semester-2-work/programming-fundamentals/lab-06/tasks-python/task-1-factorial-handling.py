# Task#1
# calculating factorial of a num & exception handling( negative num/ string) using assert.


def calculate_factorial(fact):

    assert isinstance(fact, int), f"Invalid input: '{fact}' is a string. Please enter an integer."

    assert fact >= 0, f"Invalid input: {fact} is negative. Factorial is not defined for negative numbers."

    if fact == 0 or fact == 1:
        return 1     # Base Case

    result = 1
    for x in range(2, fact + 1):
        result *= x
    return result

# Testing the program
try:
    user_entry = "haha"

    print(f"Calculating factorial for: {user_entry}")
    print(f"Result: {calculate_factorial(user_entry)}")

except AssertionError as e:
    print(f"Error: {e}")