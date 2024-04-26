'''Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue'''
try:
    x = open('wrt.txt', 'w')
    x.close()
except PermissionError:
    print("......")