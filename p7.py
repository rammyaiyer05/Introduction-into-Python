#wapp to find area of circle and circum of the circle for which radius is supplied by the user

s1=input("enter radius")
rad=float(s1)

import math
def f1():
	aoc=math.pi*rad**2
	print("areaof circle",aoc)
	print("area of circle %7.2f"%aoc)
	print("area of circle %5.2f"%aoc)
	
f1()

coc=2*math.pi*rad
print("circum of circle",coc)
print("circum of circle %8.3f"%coc)