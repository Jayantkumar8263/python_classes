'''Write a Python program to get the frequency of elements in a list '''

import collections
x = [1,2,3,4,1,2,3,4,5,6,7,8,5,6,6,8,9,0,9,8,7,6,5]
y = collections.Counter(x) 
print(y)