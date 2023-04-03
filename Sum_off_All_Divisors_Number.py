# Write a Python program to returns sum of all divisors of a number.

# Taken Input from the user
n = int(input("Enter a Number : "))
divisor = [1]

# Loop for sum of all divisor of number
for i in range(2,n):
    if n % i == 0:
        divisor.append(i)
        
print("The sum of all divisor is : ",sum(divisor))
