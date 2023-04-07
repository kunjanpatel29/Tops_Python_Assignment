# Write a python program to find the longest words.

file = open("longword.txt","w")
file.write("This is Example of Find Long Words")
file.close()

file = open("longword.txt","r")
#print(file.read())

longest_word = ""

for i in file:
    for j in i.split():
        if len(j) > len(longest_word):
            longest_word = j
        else:
            continue
    print("Longest word is: ",longest_word)

file.close()
