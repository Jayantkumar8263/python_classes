'''Write a Python program to find palindromes in a given list of strings using Lambda.'''
d = input("enter a string :")
a = list(filter(lambda x : x if d == d[::-1] else'invalid',d))
print(d)
