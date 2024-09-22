'''Write a Python program to generate all permutations(nPr = n! / (n-r)!) of a list in Python.'''

import itertools

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(itertools.permutations(x)))