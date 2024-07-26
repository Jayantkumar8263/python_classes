'''Write a  Python program to read and display the content of a given CSV file. Use csv.reader
'''
import csv
d = {
    'a' : 10, 
    'b' : 100, 
    'f' : 1000, 
    'g' : 10000,
    'h' : 100000,
    'i' : 1000000 
    }

print(csv.reader(d))