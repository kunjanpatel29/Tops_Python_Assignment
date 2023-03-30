"""
Write a Python program to find the first appearance of the substring 'not' and 'poor'
from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string.
"""

# Taken Input from the user
my_str = input("Enter a String: ")
#print(mystr)  

# Find Position
not_pos = my_str.find('not')
poor_pos = my_str.find('poor')

if not_pos < poor_pos and not_pos != -1:
    new_string = my_str.replace(my_str[not_pos:(poor_pos+4)],'good')
else:   
    new_string = my_str

print("New String is : ",new_string)
