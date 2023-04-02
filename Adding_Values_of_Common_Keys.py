"""
Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400}
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}).
"""

from collections import Counter  #import Counter(It is Dict subclass Counting Hashable objects)

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}

dict3 = Counter(dict1) + Counter(dict2) # Using Counter

print(dict3)
