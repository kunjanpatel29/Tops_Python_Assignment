# Write a Python program to check if a number is positive, negative or zero.

# Taken Input from the user
n = int(input("Enter a Number: "))

# Checking Condition for a Number is positive, negative or zero
if n > 0:
    print(n,"Is a Positive Number")
elif n < 0:
    print(n,"Is a Negative Number")
else:
    print("Number is a Zero")
