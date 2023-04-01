# Write a Python program to unzip a list of tuples into individual lists.

# Define list of tuple
my_list = [(10,40), (60,90), ("Python","C++"),(2.5,9.2),("True","False")]
print("tuple into list is: ",my_list)

# Unzip list of tuple into individual list
for item in my_list:
    print([item])

# print(list(zip(*my_list))) #Use Zip Function
