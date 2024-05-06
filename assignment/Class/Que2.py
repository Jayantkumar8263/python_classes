''' Write a Python program to create a class and display the namespace of that class '''


class name_space():
    def __init__(self, n):
        self.name = n

obj = name_space("P Jayant Kumar")
print(obj.name)