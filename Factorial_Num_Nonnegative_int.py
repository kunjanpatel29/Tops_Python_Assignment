# Write a Python function to calculate the factorial of a number (a nonnegative integer).
# Factorial = 6*5*4*3*2*1

# Function For Find Factorial of Number
def factorial(num):

    factorial = 1
    for i in range(num):
        factorial = factorial * num
        num = num - 1
    print(factorial)
        
# Taken Input from the user
num = int(input("Enter Factorial of a Number : "))
print("The Factorial of",num,"is : ",end='')
factorial(num) 

