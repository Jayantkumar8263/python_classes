'''   Write a Python program to execute a string containing Python code.'''
x = 'print("HI THERE")'
y = """
def multiply(x,y):
    return x*y
print('multiple of 9 and 7 is: ',multiply(9,7))
"""
exec(x)
exec(y) 