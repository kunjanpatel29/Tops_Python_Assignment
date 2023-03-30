#Write a Python function that takes a list of words and returns the length of the longest one.

# Define Empty List
my_list = []

# Taken Input from the user
n=int(input("Enter Length of list : "))
for i in range(n):
    value=input("Enter a List of Elements : ")
    my_list.append(value)

# Function for return the length of longest one from the words
def count_word_length(my_list):
    counter = 0
    for item in my_list:
        if len(item) >= counter:
            counter = len(item)
    return counter

print("Longest Word Length is: ",count_word_length(my_list))
