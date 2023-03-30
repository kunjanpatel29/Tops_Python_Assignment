# Write a Python program to remove duplicates from a list.

# Taken Input From the user
#my_list = list(map(int,input("\nEnter the List of Elements : ").split()))

# Define list
my_list = [10,20,30,50,90,50,9.4,10,8,20]

# Convert list to set and then remove duplicates from the list
print(sorted(set(my_list)))
