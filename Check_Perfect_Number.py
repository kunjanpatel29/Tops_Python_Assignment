# Write a Python function to check whether a number is perfect or not.

# Taken Input from the user
n = int(input("Enter a Number : "))

# Function for check Number is Perfect or not
def check_perfect_num(n):
    sum = 0
    for i in range(1,n):    # loop Till 1 to Number
        if n % i == 0:      # Check if divided by any Number    
            sum = sum + i
    return sum == n

if check_perfect_num(n) == True:
    print(n,"is a Perfect Number")
else:
    print(n,"is not a Perfect Number")
