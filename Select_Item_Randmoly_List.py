# Write a Python program to select an item randomly from a list.

# Import Random Module
import random

my_list = [1,2,3,"Python",5,7,False,9.9,15.5,"Java",True]
print("Random Element From the list is: ",random.choice(my_list))


# Using Function
"""
from random import choice

my_list = [1,2,3,"Python",5,"Hello",7,False,9.9,15.5,"Java",True]  
def random_element(my_list):
    return choice(my_list)
print("Random Element From the list is: ",random_element(my_list))
"""

