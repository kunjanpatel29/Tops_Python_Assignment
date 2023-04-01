"""
Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers
between 1 and 30.
"""

# Define Empty List
my_list = []

# Function For Print First & Last Five Element of Square between 1 to 30
def first_Last_elementsquare():
    
    for i in range(1,31):
        my_list.append(i**2)

    print("My List is :",my_list)
    print("First Five Element of Square is : ",my_list[:5])
    print("Last Five Element of Square is : ",my_list[-5:])

first_Last_elementsquare()
