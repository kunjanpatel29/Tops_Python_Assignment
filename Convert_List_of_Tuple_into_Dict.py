# Write a Python program to convert a list of tuples into a dictionary.

# Create tuples into list
my_list = [("Kunjan",90), ("Akash",60), ("Pavan",65),("Sanjay",85),("Ravi",75)]
print("my_list is : ",my_list)

my_dict = {}

# loop for convert a list of tuples into a dictionary
for i,j in my_list:
    my_dict.setdefault(i,[]).append(j)

print("Dictionary is : ",my_dict)

