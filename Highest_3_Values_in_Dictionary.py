# Write a Python program to find the highest 3 values in a dictionary.

# Create Dictionary
my_dict = {'a':200,'b':90,'c':80,'d':60,'e':40,'f':100}
print("Dictionary is : ",my_dict.values())

dic = sorted(my_dict.values())
print(dic)

print("Highest 3 values in dictionary is :",dic[-3:])
