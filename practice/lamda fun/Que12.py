'''  Write a Python program to rearrange positive and negative numbers in a given array using Lambda. '''
nums = [1, -2, 3, 4, -5, 6, -7, 8, -9, 10]
c = list(filter(lambda x : x in nums))
print(c)

bhb