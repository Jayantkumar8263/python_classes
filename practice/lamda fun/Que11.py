''' Write a Python program to find the intersection of two given arrays using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]
'''
a =  [1,2,3,4,5,6,7,8,9,10]
b =  [5,6,7,8,9,1]
c = list(filter(lambda x : x in a,b))
print("intersection ofa and b is :",c)