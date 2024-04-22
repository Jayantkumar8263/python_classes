'''Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.'''
ap = ('abcdefghijklmnopqrstuvwxyz')
for i in ap :
    open(i+'.txt','x')