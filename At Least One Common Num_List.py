#Write a Python function that takes two lists and returns true if they have at least one common member.

# Define Empty List
list1 = []
list2 = []

# Taken input from the user
a = int(input("Enter length of list1 : "))
for i in range(a):
    value = int(input("Enter a list1 Elements : "))
    list1.append(value)

b = int(input("Enter length of list2 : "))
for i in range(b):
    value = int(input("Enter a list2 Elements : "))
    list2.append(value)   

def CommonNumber(list1,list2):

    result = False
    # Traverse in 1st list
    for x in list1:
        for y in list2:  #  # Traverse in 2nd list
            if x == y:  # Check for if one element common
                result = True
                return result
    return result

print("List1 is : ",list1)
print("List2 is : ",list2)
print(CommonNumber(list1,list2))
