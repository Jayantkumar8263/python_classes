''' Write a python program to find the longest words. '''
ab = open('long.txt','r')
#ab.write("ciwuciuh wie wecweoo")
read = ab.readline()
bc = read.split()
print(max(bc, key=len))
ab.close()