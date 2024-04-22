''' Write a Python program to read first n lines of a file '''
x = int(input("enter a number :"))
a = open('abc.txt','r')
#a.write("Hi... how are you ??")
read =a.readlines()
for i in range(x):
    print(read[i])
a.close()