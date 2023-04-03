# Write a Python program to calculate surface volume and area of a cylinder.

#Volume of Cylinder = πr²h        #Surface Area of Cylinder = 2πr² + 2πrh

pi = 22/7

height = float(input('Enter Height of cylinder: '))
radius = float(input('Enter Radius of cylinder: '))

volume = pi * (radius * radius) * height
surface_area = 2 *(pi * radius * height) + 2*(pi*radius**2)

print("Volume of Cylinder is : ", volume)
print("Surface Area of Cylinder is : ", surface_area)

