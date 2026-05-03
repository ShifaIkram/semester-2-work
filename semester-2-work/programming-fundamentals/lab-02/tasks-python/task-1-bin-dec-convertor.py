# TASK#1
# BINARY TO DECIMAL CONVERTOR

# Method#1: (by using in-built function)
binary_num = input("Enter the binary number: ")
decimal_num = int(binary_num,2)
print(decimal_num)

# Method#2: (by using traditional binary conversion method)
bin_code = input("Enter a binary number: ")

# Initialization
deci = 0
pow = 0

for digit in bin_code[::-1]:    #(inverse used bcs we start converting from left)
    deci = deci + int(digit) * (2 ** pow)
    pow+=1

print(f"Decimal equivalent of {bin_code} is", deci)



