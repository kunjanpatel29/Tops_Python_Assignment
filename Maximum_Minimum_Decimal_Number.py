# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

# import decimal
from decimal import *

dec = list(map(Decimal,'3.9 0.9 1.8 12.8 22.3 8.6'.split()))

print("Max : ",max(dec)) # Max of Decimal Number
print("Min : ",min(dec)) # Min of Decimal Number
