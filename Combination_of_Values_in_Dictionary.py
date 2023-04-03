"""
Write a Python program to create and display all combinations of letters, selecting each
letter from a different key in a dictionary. Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output: ac ad bc bd 
"""

from itertools import product  # product method of the itertools module

my_dict ={'1':['a','b'], '2':['c','d']}

# Loop for Display all combinations of letters
for x,y in product(*my_dict.values()):  # product returns the cartesian product of iterables
    print(x+y,end=' ')
