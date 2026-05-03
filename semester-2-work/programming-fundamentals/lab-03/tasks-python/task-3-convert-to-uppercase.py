# TASK#3
# Convert String to Uppercase using lambda function and also invert it

# Take string input from the user
string = input("Enter a string: ")

# Convert Input String to uppercase using lambda func
upper_case = lambda s: s.upper()

upper_string = upper_case(string)

print("Uppercase string:", upper_string)

# User Defined Function to reverse the string
def invert(s):
    print("Reversed string:", s[::-1])

# Call the UDF
invert(upper_string)