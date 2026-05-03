# To print Pattern(asterisk)

# First part: increasing asterisk pattern
for i in range(1, 5):   # 1 to 4
    for j in range(i):
        print("*", end=" ")
    print()  # Move to next line

# Second part: decreasing asterisk pattern
for i in range(3, 0, -1):  # 3 to 1
    for j in range(i):
        print("*", end=" ")
    print()  # Move to next line