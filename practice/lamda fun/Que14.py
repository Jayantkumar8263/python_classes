''' Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda. '''
names = ["jayant",'stevo','vasu','pratul','vaibhav','janvi']
friends = list(filter(lambda x : x if len(names) == 6 else '',names))
for f in friends:
    print(f)