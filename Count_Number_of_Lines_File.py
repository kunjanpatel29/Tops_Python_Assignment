# Write a Python program to count the number of lines in a text file. 

file = open("random_file.txt","r")
#print(file.read())

count = 0

for i in file:
    count = count + 1
print("Number of line in file is : ",count)
    
file.close()
