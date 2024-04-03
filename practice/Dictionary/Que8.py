''' 8. Write a Python script to merge two Python dictionaries. '''
d = {
    'name' : 'P Jayant Kumar'
     }
d1 = {
    'mobile' : 987456321
}
d2 = d.copy()
d2.update(d1)
print(d2)
