# Write a Python script to concatenate following dictionaries to create a new one. 

# Create Dictionary
dict1 = {'a':10,'b':20}
dict2 = {'c':30,'d':40}
dict3 = {'e':50,'f':60}

dict4 = {}

# loop for Concatenate Dictionary 
for d in dict1,dict2,dict3:
    dict4.update(d)

print("Dictionary is : ",dict4)

