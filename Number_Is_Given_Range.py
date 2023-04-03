# Write a Python function to check whether a number is in a given range.

# Taken Input from the user
n = int(input("Enter a Number Between 1 to 30 : "))

# Function For Check Number is in given range
def check_num_in_range(n):
    if n in range(1,31):
        print(n,"is in range")
    else:
        print(n,"is not in range")

check_num_in_range(n)
