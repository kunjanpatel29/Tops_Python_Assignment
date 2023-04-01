# Write a Python program to check whether a list contains a sub list.

# Define list
my_list=["a","b",[10,20,"Hello",4.5],1,2]

# Check for list contains sublist or not
for i in my_list:
        if len(i) > 1:
                print("Sublist is present in list")
                break
else:
        print("Sublist is not present in list")

