a = float(input("enter a amount :"))
r = float(input("enter rate of interest :"))
t = float(input("enter time :"))
SI = a*r*t/100
CI = a*(1+r/100)**t
print(SI)
print(CI)