''' 20. Write a Python program to remove the intersection of a second set with a first set. '''
x = {1, 2, 3, 4, 5}
y = {3, 4, 5, 6, 7}

for i in x.intersection(y) :
    x.remove (i)
print(x)
