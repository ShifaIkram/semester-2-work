# Task#1
#Taking list from user,remove duplicates,append only unique elements in new list

# Taking input list from user
user_list = input("Enter elements separated by space: ").split()

# Creating a new list for unique elements
unique_list = []

# Using loop to remove duplicate from the user_list
[unique_list.append(x) for x in user_list if x not in unique_list]

# Displaying result
print("List after removing duplicates:", unique_list)