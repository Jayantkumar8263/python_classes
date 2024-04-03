'''Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number. '''
x = int(input("enter a number :"))
a = [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    for j in range(i+1, len(a)):
        for k in range(i+2, len(a)):
            if a[i]+a[j]+a[k] == x:
                print(a[i],a[j],a[k])