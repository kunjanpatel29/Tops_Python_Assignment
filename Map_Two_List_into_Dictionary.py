# Write a Python program to map two lists into a dictionary 

# Create List
languages = ["Python","Java","Javascript","PHP"]
version = [3,15,4,5]

my_dict = dict(zip(languages,version))  # Use Zip function
print("Dictionary is : ",my_dict)
