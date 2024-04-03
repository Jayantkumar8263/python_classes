''' Write a Python program to print the even numbers from a given list. '''
def even(e):
    x = []
    for i in e:
        if i % 2 == 0 :
           x.append(i)
    return x

print(even([1,2,3,4,5,6,7,8,9,10]) )
#even(i)