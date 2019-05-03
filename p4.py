#wapp to find max and min from elements provided by the user

import array
num=array.array('i',[])

n=int(input("enter the number of elements"))
for i in range(n):
	ele=int(input("enter the element"))
	num.append(ele)

max=min=num[0]
for i in range(len(num)):
	if num[i]>max:
		max=num[i]
	if num[i]<min:
		min=num[i]
print("Max",max,"Min",min)