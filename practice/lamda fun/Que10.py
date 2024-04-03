''' Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
'''
from functools import reduce
a  = lambda x: reduce(lambda x,_ : x + [x[-1] + x[-2]], range(x - 2), [0, 1])
print("Fibonacci series upto 2 :")
print(a(11))
