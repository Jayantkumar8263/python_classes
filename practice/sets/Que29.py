'''29. Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type.
'''
a = [0,1,2,3,4,5,6,7,8,9,10,11,12]
for i in range (12):
    for j in range(i-1 ,len(a)):
        for k in range(i-2 , len(a)):
            print()