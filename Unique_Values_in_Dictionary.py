# Write a Python program to print all unique values in a dictionary.

# Create Dictionary
my_dict = {'a':20,'b':60,'c':30,'d':20,'e':50,'f':30,'g':60}

print("Dictinary values : ",sorted(my_dict.values()))
print("Unique Values in Dictionary",sorted(set(my_dict.values())))
