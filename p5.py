#wapp to find the sum of digits provided by the user

num=int(input("enter a number"))
sum=0

while num>0:
	digit=num%10
	sum=sum+digit
	num=num//10
print("sod",sum)