''' Write a Python function that takes a list and returns a new list with distinct elements from the first list '''    
def pqr(p):
    x = []
    for a in p :
        if a not in x :
            x.append(a)
    return x
print(pqr([1,2,2,3,3,3,4,4,4,4]))     