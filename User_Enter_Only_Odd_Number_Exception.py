# Write python program that user to enter only odd numbers, else will raise an exception. 

n = int(input("Enter a Number : "))

if n % 2 == 0:
    raise ValueError("Please Enter Only Odd Number")
else:
    print(n," Is a Odd Number")
