# Write a Python program to convert a list of characters into a string.

# Define List
my_list = ["H","e","l","l","o"]

# Function For convert a list of characters to a string. 
def convert_ch_to_string(my_list):

    mystr = ""
    return(mystr.join(my_list))

print("Convert List of Character to String is :",convert_ch_to_string(my_list))


"""
list1 = []
n=int(input("Enter Length of list : "))

for i in range(n):
    value=input("Enter a Character : ")
    list1.append(value)

for i in list1:
    print(i,end="")
"""
