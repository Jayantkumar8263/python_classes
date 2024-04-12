''' Write a Python program to copy the contents of a file to another file '''
a = open('abc.txt','r')
b = a.readline()
print(b)
c = open('def.txt','a')

c.write(b)