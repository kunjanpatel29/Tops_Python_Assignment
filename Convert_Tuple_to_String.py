# Write a Python program to convert a tuple to a string.

# Function For Convert Tuple to String
def convert_tuple_to_string(mytuple):
    mystr = ""
    for item in mytuple:
        mystr = mystr + item
    return mystr

mytuple = ('P','y','t','h','o','n')
print(convert_tuple_to_string(mytuple))
