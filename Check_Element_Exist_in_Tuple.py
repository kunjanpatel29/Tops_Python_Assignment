# Write a Python program to check whether an element exists within a tuple.

# Define Tuple
my_tuple = (15,25,45,75,60,35,95,85,90)
print(my_tuple)

print(95 in my_tuple)
print(25 in my_tuple)

# Taken input from the user
element=int(input("Enter a Element for check : "))
for i in my_tuple:
    if i == element:
        print(element,"is Exists in Tuple")
        break
else:
    print(element,"is Not Exists in Tuple")
