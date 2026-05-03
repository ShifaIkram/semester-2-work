# Task#3
# Checking for Palindrome Numbers

# Taking input from the user
num = input("Enter a number: ")

# Reverse num by Slicing
reverse_num = num[::-1]    #reverses the string(backwards)

# Check if og and reverse are same or not
if num == reverse_num:
    print("The number is a Palindrome Number.")
else:
    print("The number is not a Palindrome Number.")