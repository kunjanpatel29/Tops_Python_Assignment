# Write a Python program to find the repeated items of a tuple. 

# Define Tuple
my_tuple = (1,5,19,29,64,1,3,2,5,5,2)
print("my_tuple is : ",my_tuple)

# Return the number of repeated items appear in the tuple
count=my_tuple.count(int(input("Enter item to count repeat : ")))
print("Total Count is : ",count)
