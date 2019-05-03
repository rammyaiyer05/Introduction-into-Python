#wapp to find factorial of a number provided by the user

num=int(input("enter a number:"))

if(num<0):
	print("enter positive number")
elif(num==0):
	print("ans=",1)
else:
	fact=1
	for i in range(1,num+1):
		fact=fact*i
	print("ans=",fact)