#wapp for pattern generation

num=int(input("enter the number of lines:"))

for i in range(num):
	for j in range(i+1):
		print("*",end=' ')
	print()