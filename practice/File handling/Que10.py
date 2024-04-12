''' Write a Python program to count the frequency of words in a file. '''
x = open('abc.txt','r')
y = x.readlines()
for i in range(5):
    print(len(y[i])) 
    x.close()