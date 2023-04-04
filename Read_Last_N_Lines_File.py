# Write a Python program to read last n lines of a file.

file = open("random_file.txt","r")

n = int(input("Enter for last N Lines : "))

for i in (file.readlines() [-n:]):
    print(i,end='')
