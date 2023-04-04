# Write a Python program to read a file line by line and store it into a list.

file = open("mylistfile.txt","w")
file.write("Python\n")
file.write("Java\n")
file.write("HTML\n")
file.write("JavaScript\n")
file.write("PHP\n")
file.close()

file = open("mylistfile.txt","r")
f = file.readlines()

my_list = []
for i in f:
    my_list.append(i)
    print(i,end="")

print(my_list)
file.close()
    
