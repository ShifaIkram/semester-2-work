#TASK#4
# Random password Generator
import random

# Take input from user
length = int(input("Enter the length of password: "))

upper_case = input("Do you want to include uppercase letters? (y/n): ")
lower_case = input("Do you want to include lowercase letters? (y/n): ")
digits = input("Do you want to include digits? (y/n): ")
special_char = input("Do you want to include special characters? (y/n): ")

#initialization
characters = ""

# Adding characters according to user choice
if upper_case.lower() == "y":
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if lower_case.lower() == "y":
    characters += "abcdefghijklmnopqrstuvwxyz"

if digits.lower() == "y":
    characters += "0123456789"

if special_char.lower() == "y":
    characters += "$*!%^#@"

# To check if even one of the options is selected
if characters == "":
    print("You must select at least one type of character.")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Your Generated Password:", password)