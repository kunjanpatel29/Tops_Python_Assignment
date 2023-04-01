# Write a Python program to get unique values from a list. 

# Define Empty List
list1 = []
list2 = []

# Taken Input from the user
n=int(input("Enter Length of List : "))
for i in range(n):
    value=int(input("Enter List of Elements : "))
    list1.append(value)
print("List is : ",list1)
    
# Use For loop
for value in list1:
    if value not in list2:
        list2.append(value)

print("Unique Values from list using append : ",list2)
    
