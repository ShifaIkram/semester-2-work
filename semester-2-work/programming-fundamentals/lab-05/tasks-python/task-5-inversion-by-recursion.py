# Task #5
# Recursive function to reverse string

# Method#1:  Using Slicing
# Making function
def rev_string(s):
    if s == "":   # Base Case
        return s
    return rev_string(s[1:]) + s[0]

# Taking input
Input = input("Enter a string:")

# Calling the actual function
String = rev_string(Input)

# Final Result
print("Reversed string:", String)

# Method#2:  Using Indexing Method
# Making function
def reverse_string(s, i):
    if i < 0:        # Base Case
        return ""
    return s[i] + reverse_string(s, i - 1)

# Taking input
text = input("Enter a string:")

# Calling function (starting from last index)
string = reverse_string(text, len(text) - 1)

 # Result:
print("Reversed:", string)

