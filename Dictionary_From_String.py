"""
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output : {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""

# Taken Input from the user
my_str = input("Enter a String : ")

my_dict = {} # Create Empty Dictionary

for i in my_str:
    if i in my_dict:
        my_dict[i] = my_dict[i] + 1
    else:
        my_dict[i] = 1

print("Dictionary from string is : ",my_dict)
