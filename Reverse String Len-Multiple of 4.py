# Write a Python function to reverses a string if its length is a multiple of 4.

# Using Function
def string_reverse(mystr):
    if len(mystr) % 4 == 0: # For check if reverse string its length is a multiple of 4
       print(''.join(reversed(mystr)))
    else:
        print("Please Enter a Valid Length !!")

# Taken Input from the user
mystr = input("Enter String: ")
string_reverse(mystr)
