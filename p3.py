#wapp for pattern generation

num=int(input("enter the number of lines:"))

k=65
for i in range(num):
	for j in range(i+1):
		print(chr(k),end=' ')
	print()
	k=k+1