# Write a Python program to check a list is empty or not.

# Taken Input from the user
#my_list = list(map(int,input("Enter List of Elements: ").split()))
#print(my_list)

my_list = [10,20,30,40,50,60,70,80]

# Checking for the Condition list is empty or not
if not my_list:
    print("List is Empty")
else:
    print("List is Not Empty \n",my_list)
