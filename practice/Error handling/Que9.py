'''Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.'''
try:
    a = open('aqz.txt','w')
    a.close()
except:
    raise UnicodeDecodeError