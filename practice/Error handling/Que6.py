'''Write a  Python program that executes an operation on a list and handles an IndexError exception if the index is out of range '''
try:
    x = ["abc","def",1, 2, 3, 4, 5]
    print(len(x))
except:
    raise IndexError
print("....")
        