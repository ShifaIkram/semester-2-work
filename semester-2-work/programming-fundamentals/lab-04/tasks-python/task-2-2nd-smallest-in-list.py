# Task#2
# Finding 2nd Smallest element(specifically num) from the entered num list

# Taking input list from user
user_list = [int(x) for x in input("Enter numbers separated by space: ").split()]

# Removing duplicates so that indexing could be done proper later
unique_list = list(set(user_list))  # set = unordered (so use list)
                                     # removes duplicates (stores unique values only)

if len(unique_list) < 2:
    print("There is no second smallest element.")
else:
    unique_list.sort()
    print("Second smallest element is:", unique_list[1])

