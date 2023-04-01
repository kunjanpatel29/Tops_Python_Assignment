# Write a Python program to replace last value of tuples in a list.

# Define tuple in a list
my_list = [(10, 20, 30, 40, 50, 60)]
print("my_list is : ",my_list)

for i in my_list: 
    print(i[:-1] + (100,)) # In Tuple Last Index add 100
