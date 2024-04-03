''' Write a Python program to remove an item from a tuple. '''
x = (0, 'j', 1, 2, 3, 4, 5, 7, 8, 9)
x=list(x)
print(x)
x.remove(2)
x = tuple(x)
print(x)