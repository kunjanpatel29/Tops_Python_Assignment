# Write a Python script to merge two Python dictionaries.

# Create Dictionary
d1 = {'a': 10, 'b': 20,'c':30,'d':40}
d2 = {'k': 60, 'n': 80}

d3 = d1.copy() # Copy Dictionary d1 into d3
d3.update(d2) # Added dictionary d2 into the end of d1

print("Dictionary is : ",d3)
