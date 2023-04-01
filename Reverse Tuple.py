# Write a Python program to reverse a tuple.

# Define tuple
my_tuple = (1,9,45,36,"Python",True,9.6,5,"Hello")
print("Before Reverse tuple is : ",my_tuple)
my_tuple = my_tuple[::-1]  # Using Slicing
print("After Reverse tuple is : ",my_tuple)

# Using Reversed method
#my_tuple = tuple(reversed(my_tuple))
#print("Reversed Tuple is : ",my_tuple)
