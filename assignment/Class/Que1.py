''' Write a  Python program to import a built-in array module and display the namespace of the said module '''

import array
class name_space():
    def __init__(self, name):
        self.name = name
obj = name_space("jayant")
print(obj.name)