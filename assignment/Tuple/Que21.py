''' Write a Python program to remove an empty tuple(s) from a list of tuple
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')] '''
a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
b =  a.remove(())
print(a)