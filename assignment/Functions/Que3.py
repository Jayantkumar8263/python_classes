''' Write a Python function to multiply all the numbers in a list. '''
def ab(a, b):
    b = (a, b)
    x = 1
    for i in b:
        x*= i
    return x
print(ab(4, 5))
        