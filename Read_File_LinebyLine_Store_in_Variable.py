# Write a Python program to read a file line by line store it into a variable.

file = open("random_file.txt","r")

f = file.readlines()
#print(f)

for i in f:
    print(i,end='')
file.close()
