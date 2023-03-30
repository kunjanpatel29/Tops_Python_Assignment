"""
Write a Python program to count the number of strings where the string length is 2 or more and the first
and last character are same from a given list of strings.
"""

count = 0    # Initialize count to 0
my_list = [] # Define Empty List

# Taken Input from the user
x = int(input("Enter length of list : "))
for i in range(x):
    value = input("Enter a Elements in list : ")
    my_list.append(value)

# Checking for count the number of strings where first and last character is same
for words in my_list:
    if len(words) > 2 and words[0] == words[-1]:
        print("The Words in given list are: ",words)
        count = count + 1

print("Number of words you want list First and last character same is : ",count)

