''' Write a Python program to read a file line by line store it into a variable. '''
ac = open('bcd1.txt','r')
#ac.write('a = jay, i am a 18')
read = ac.readline()
print(read)
ac.close()