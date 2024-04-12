''' Write a Python program to assess if a file is closed or not. '''
a = open('abc.txt','r')
print(a.closed)
a.close()
print(a.closed)