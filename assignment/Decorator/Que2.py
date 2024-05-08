'''Write a  Python program to create a decorator function to measure the execution time of a function.'''

def my_decorator(func):
    def wrapper(*args, **kwars):