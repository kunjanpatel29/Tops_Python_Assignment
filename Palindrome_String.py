# Write a Python function that checks whether a passed string is palindrome or not.
# Example : madam, level 

# Taken Input from the user
my_str = input("Enter String : ")

# Function For Check a passed string is palindrome or not
def check_palindrome(my_str):
    if(my_str == my_str[::-1]):
        return "The String is Palindrome"
    else:
        return "The String is Not Palindrome"
    
print(check_palindrome(my_str))


# Using loop
"""
my_str = input("Enter String : ")

reverse_str = ""

for i in my_str:
    reverse_str = i + reverse_str
print("Reversed String is :",reverse_str)

if(my_str == reverse_str):
    print("The String is Palindrome")
else:
    print("The String is Not Palindrome")
"""
