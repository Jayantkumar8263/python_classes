''' Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist '''
try:
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
except AttributeError:
    print("an AttributeError has occurd")