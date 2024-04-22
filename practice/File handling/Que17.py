''' Write a Python program to remove newline characters from a file. '''
d = open('abc.txt','r')
e = d.read()
f = e.rstrip(['\n'])
print(f)
d.close()