'''Write a Python program to create a shallow copy of a given dictionary. Use copy.copy'''

import copy
x = {
    'a' : 10, 
    'b' : 100, 
    'f' : 1000, 
    'g' : 10000,
    'h' : 100000,
    'i' : 1000000 
}
print(copy.copy(x))