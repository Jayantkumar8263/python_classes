'''. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the lambda function.
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48
'''
nums = [ 2, 4, 6, 8, 10, -1, -3, -5, -7, -9]
posative_nums = list(filter(lambda nums : nums > 0, nums))
negative_nums = list(filter(lambda nums : nums < 0, nums))
print("sum of posative numbers is :", sum(posative_nums))
print("sum of negative numbers is :", sum(negative_nums))