# Write a Python program to check multiple keys exists in a dictionary.

# Create Dictionary 
my_dict = {
    'a':10,
    'b':20,
    'c':30,
    'd':40
}
print("keys are : ",my_dict.keys())

# Check Multiple Key Exists or not Using Comparison Operator
print(my_dict.keys() >= {'a', 'c'})
print(my_dict.keys() >= {'b', 'e'})


"""
count = 0
for i in my_dict:
    if i == "":
        break
    else:
        count = count + 1

print(count, "Keys are present in dictionary")
"""
