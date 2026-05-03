#TASK#2
# Largest num b/w 2 num using lambda func

# Take 2 numbers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#  Lambda function to find the larger number
larger_num = lambda num1,num2: num1 if num1 > num2 else num2

print("The larger of the two numbers is:", larger_num(num1, num2))

# Step 3: User Defined Function to print table
def table(num, range_lim):
    print(f"\nTable of {num}:")
    for i in range(1, range_lim + 1):
        print(f"{num} x {i} = {num * i}")

# Step 4: Ask user for range for the table
limit = int(input("Enter the range for table: "))

# Step 5: Call UDF
table(larger_num(num1, num2), limit)   # limit=range_lim , num=larger_num



