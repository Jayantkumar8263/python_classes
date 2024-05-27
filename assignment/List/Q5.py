''' Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same '''

a = input("Enter the list of string :")
if len(a) >= 2 or a[0] == a[:-1] : 
    print('ok')
else:
    print('invalid')