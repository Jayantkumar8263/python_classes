'''3. Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
'''
d1 = {1, 2, 3}
d2 = {3, 5, 6}
d3 = {7, 8, 9}
d4 = {}
for d in (d1, d2, d3):
    d4.update(d)
print(d4)