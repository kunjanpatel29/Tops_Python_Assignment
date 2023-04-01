# Write a Python function that takes a list and returns a new list with unique elements of the first list. 

# Defined Empty List
my_list = []

# Taken Input from the user
n=int(input("Enter Length of List : "))
for i in range(n):
    value=int(input("Enter List of Elements : "))
    my_list.append(value)
print("Before List is: ",my_list)

def unique_element(my_list):
    my_list = sorted(set(my_list)) # Convert list to set for remove Duplicate Element
    print("List of Unique Number in list is: ",my_list)
unique_element(my_list)
