'''Write a Python program to create a shallow copy of a given list. Use copy.copy '''

import copy
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b = copy.copy(x)
print(b)