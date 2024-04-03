''' Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda '''
nums = [19,13,26,39,38,57]
a = list(filter(lambda x : x % 13 == 0,nums))
b = list(filter(lambda x : x % 19 == 0,nums))
print("numbers which are devisible by 13 are :",a)
print("numbers which are devisible by 19 are :",b)