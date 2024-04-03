'''Write a Python program to read an entire text file. '''
a = open('eve.txt','r')
#a.write("Hi fan")
read =a.read()
print(read)
a.close() 