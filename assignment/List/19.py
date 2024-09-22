'''Write a Python program to calculate the difference between the two lists.'''

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [10, 9, 8, 7, 6, 1]
a = set(x)
b = set(y)
d = a - b
print(list(d))