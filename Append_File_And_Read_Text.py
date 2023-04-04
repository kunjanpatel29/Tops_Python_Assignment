# Write a Python program to append text to a file and display the text.

file = open("file.txt","a")
string = input("\nEnter Data to Append In Text File : ")
file.write(string + "\n")
file.close()

file = open("file.txt","r")
print(file.read())
file.close()
