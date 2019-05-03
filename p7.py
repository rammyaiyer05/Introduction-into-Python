t=int(input("Enter the number of test cases:"))
temp=''
msg=input("Enter your message:")
print(len(msg))
ss=list(msg)
if ss%2==0:
	for i in range(len(ss)):
		if i%2==0:
			temp+=ss[i].upper()
		else:
			temp+=ss[i].lower()
else:
	for i in range(len(ss)):
		if 
print(temp)