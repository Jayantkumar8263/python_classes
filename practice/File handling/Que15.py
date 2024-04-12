''' Write a Python program to read a random line from a file. '''
import random
x = open('eve.txt','r')
y = x.read().splitlines()
print(random.choice(y))
x.close()