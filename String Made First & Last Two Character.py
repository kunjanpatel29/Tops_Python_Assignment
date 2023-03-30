"""
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a
string. If the string length is less than 2, return instead of the empty string.
"""

# Taken Input from the user
mystr = input("Enter a String : ")

# Function For get a string made of the first 2 and the last 2 chars from a given a string
def GetFirstLastTwoCharacter(mystr):
    if len(mystr) < 2:
        return " "
    return mystr[0:2] + mystr[-2:]

print("New String is : ",GetFirstLastTwoCharacter(mystr))
