# Task#4
# Program to input 3x3 matrix, display it and its transpose

# Step 1: Take 3 rows as input
matrix = []

print("Enter 3 rows of 3 numbers each:")

for i in range(3):
    row = [int(x) for x in input(f"Row {i+1}: ").split()]
    if len(row) != 3:
        print("Please enter exactly 3 numbers!")
        exit()
    matrix.append(row)

# Step 2: Display the og Matrix
print(" \nOriginal 3x3 Matrix: ")
for row in matrix:
    print(row)

# Step 3: Calculate the Transpose
transpose = [[matrix[j][i] for j in range(3)] for i in range(3)]

# Step 4: The Transpose
print("\nTranspose of the matrix:")
for row in transpose:
    print(row)

