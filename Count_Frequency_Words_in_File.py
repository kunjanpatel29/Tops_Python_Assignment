# Write a Python program to count the frequency of words in a file.

file = open("test.txt","w")
file.write("Kunjan Patel\n")
file.write("Pritesh Shah\n")
file.write("Sanjay Patel\n")
file.write("Maulik Shah\n")
file.close()

file = open("test.txt","r")

d = {}

for i in file:
    words = i.split(" ")
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

print("Frequency of words Count in a file is : ",d)
file.close()
