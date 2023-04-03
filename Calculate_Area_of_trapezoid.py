# Write a Python program to calculate the area of a trapezoid.

# Taken Input from the user
height = float(input("Enter Height of Trapezoid : "))
base1 = float(input('Enter Base value for one : '))
base2 = float(input('Enter Base value for two : '))

# Calculate the area
area = (base1 + base2)/2 * height

print("Area of Trapezoid is : ",area)
