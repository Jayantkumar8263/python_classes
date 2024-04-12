''' Write a Python program to read first n lines of a file. '''
a = open('abc.txt','+r')
#a.write("Hi... how are you ??")
read =a.readlines()
print(read)
a.close()