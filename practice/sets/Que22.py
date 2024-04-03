''' 22. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
'''
x = int(input("entre the number :"))
a = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(11):
    for j in range(i+1, len(a)):
        if a[i]+a[j] == x:
            print(a[i],a[j])
            
        
            
