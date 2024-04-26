'''Write a  Python program that opens a file and handles a FileNotFoundError exception if the file 
does not exist'''
try:
    a  = open("wrt.txt", "w")
    b = a.write(".....")
    a.close()
except FileNotFoundError:
    print("Error")