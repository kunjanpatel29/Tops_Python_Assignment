# Write a Python script to check if a given key already exists in a dictionary. 

# Create Dictionary
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd':40,'e':50,'f':90}
print("Dictionary is : ",my_dict)

n=input("Enter Key for check : ")

# Function for check given key exists or not
def check_key_present(n):

  for i in my_dict:
    if i == n:
      print('Key is present in the dictionary')
      break
  else:
      print('Key is not present in the dictionary')
      
check_key_present(n)
