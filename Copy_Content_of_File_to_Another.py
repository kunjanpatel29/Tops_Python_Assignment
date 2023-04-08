# Write a Python program to copy the contents of a file to another file.

# open both files
with open("mylistfile.txt","r") as f:
    with open("copyfile.txt", "w") as f1:
        # read content from first file
        for line in f:
            # write content to second file
            f1.write(line)
        print("Content Copied in another File Successfully")
