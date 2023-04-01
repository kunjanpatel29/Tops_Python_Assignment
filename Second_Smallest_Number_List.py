# Write a Python program to find the second smallest number in a list.

# Define list
my_list = []

# Taken Input from the user
n=int(input("Enter Length of List : "))
for i in range(n):
    value=int(input("Enter List of Elements : "))
    my_list.append(value)

my_list.sort() # Sort the list Elements
print("The sorted list: ", my_list) 
print("The second smallest Element from list is : ",my_list[1])

