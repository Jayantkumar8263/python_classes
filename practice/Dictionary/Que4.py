''' 4. Write a Python script to check whether a given key already exists in a dictionary. '''
x = input("enter the keys :")
d = {
    'red' : 1,
    'blue' : 2,
    'green' :3,
}
if x in d :
    print("True")
else:
    print("False")
    