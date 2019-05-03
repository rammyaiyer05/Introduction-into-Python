#wapp to reverse the given num

num=int(input("enter a number"))
rev=0
n1=num%10
while num>0:
	digit=num%10
	rev=rev*10+digit
	num=num//10
if(n1==0):
	print("rev:" ,0,rev,sep='')
else:
	print("reverse",rev)