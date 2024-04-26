''' Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical. '''
try:
    x = int(input("enter a number :"))
    y = int(input("enter a number :"))
except :
    raise TypeError
