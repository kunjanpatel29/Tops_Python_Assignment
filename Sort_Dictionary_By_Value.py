# Write a Python script to sort (ascending and descending) a dictionary by value.

import operator

my_dict = {"a":60, "b":90, "c":30, "d":50}

print('Original dictionary : ',my_dict)

my_dict_sort = sorted(my_dict.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',my_dict_sort)

my_dict_sort1 = dict( sorted(my_dict.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',my_dict_sort1)
