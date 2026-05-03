# TASK#4
# TEMPERATURE CONVERTOR PROGRAM (C & F)

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    c = (f - 32) * 5 / 9
    return c

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f

# Ask user what they want to convert
choice = input("Enter 1 to convert F to C or 2 to convert C to F: ")

if choice == "1":
    enter = float(input("Enter temperature in Fahrenheit: "))
    temp = fahrenheit_to_celsius(enter)
    print("Temperature in Celsius:", temp)
elif choice == "2":
    enter = float(input("Enter temperature in Celsius: "))
    temp = celsius_to_fahrenheit(enter)
    print("Temperature in Fahrenheit:", temp)
else:
    print("Invalid choice")