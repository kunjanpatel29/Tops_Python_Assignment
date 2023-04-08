# Write a Python program to write a list to a file. 

my_list = ["First","Second","Third","Fourth"]

with open("list.txt","w") as f:
    for i in my_list:
        f.write("%s\n" % i)
    print("Write list to a file Successfully")
