# Write a Python program to read first n lines of a file. 

from itertools import islice

n = int(input("Enter for First N Lines : "))

f = open("random_file.txt","r")

for i in islice(f,n):
    print(i,end='')
    
