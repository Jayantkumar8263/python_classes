''' Write a Python program to filter a list of integers using Lambda. 
Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]'''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even = list(filter(lambda x: x % 2 == 0,nums))
is_odd = list(filter(lambda x: x % 2 != 0,nums))

print("Even numbers are :", is_even)
print("Odd numbers are:", is_odd)