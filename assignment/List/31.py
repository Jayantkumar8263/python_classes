'''Write a Python program to count the number of elements in a list within a specified range '''

import collections
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for i in range(x[6]):
    print(collections.Counter(x))