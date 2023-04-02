# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

# Create Empty Dictionary
my_dict = {}

for i in range(1,16):
    my_dict[i] = i*2   # Keys are 1 to 15 and value assigned as double

print("Dictionary is : ",my_dict)
