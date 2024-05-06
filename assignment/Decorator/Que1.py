''' Write a  Python program to create a decorator that logs the arguments and return value of a function. '''


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'{args}', {**kwargs})
        func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function(a,b):
    print(a+b)
    
x = int(input("Enter a number :"))
y = int(input("Enter a number :"))

my_function(x,y)