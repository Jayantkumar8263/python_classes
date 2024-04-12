''' Write a Python program that takes a text file as input and returns the number of words of a given text file '''
y = input("enter file name :")
var = open(y,'r')
z = var.read().split()
print(len(z))