''' Write a Python program to add two given lists using map and lambda. '''
a = [0,1,2,3,4]
b = [5,6,7,8,9]
c = list(map(lambda x, y  : x + y, a, b))
print(c)