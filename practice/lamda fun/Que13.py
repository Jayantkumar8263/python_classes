'''Write a Python program to count the even and odd numbers in a given array of integers using Lambda. '''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(filter(lambda x : x % 2 == 0,nums))
b = list(filter(lambda x : x % 2 != 0,nums))
print("Even numbers are :",len(a))
print("odd numbers are :",len(b))