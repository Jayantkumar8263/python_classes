''' Write a Python program to read a file line by line and store it into a list. '''
a = open('bcd.txt','r')
#a.write("[Hi.... Jayant!!!]")
read = a.readline()
print(read)
a.close()