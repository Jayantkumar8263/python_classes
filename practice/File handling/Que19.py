''' Write a Python program to extract characters from various text files and puts them into a list. '''
a = open('abc.txt', 'r')
b = a.readline()
c = open('bcd.txt', 'r')
d = c.readline()
v = []
print(b)
a.close()
c.close()