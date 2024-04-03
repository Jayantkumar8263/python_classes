'''Write a Python program that multiplies each number in a list with a given number using lambda function .'''
a = int(input("Enter a number :"))
nums = [0,1,2,3,4,5,6,7,8,9,10]
x = list(lambda x : x * nums,a)
print(a)