# TASK# 3
# Program to display prime numbers in a given range and their sum

# Take input(number range) from the user
range_start = int(input("Enter start of the range: "))
range_end = int(input("Enter the end of the range: "))

total_sum = 0

print("Prime numbers are:")

for num in range(range_start, range_end + 1): # end num is exclusive so +1

    if num > 1:        # Prime num start from 2 so >1
        is_prime = True

        for i in range(2, num):  #checks divisibility of num b/w 2 and num-1
            if num % i == 0:
                is_prime = False  # if num is divisible by any other num
                break             # other than 1 and itself

        if is_prime:
            print(num)
            total_sum = total_sum + num

print("Sum of prime numbers:", total_sum)