#wamdp to implement FIFO/stack

import array
st=array.array("i",[])

while True:
	opt=int(input("1.push,2.pop,3.peek,4.display,5.exit"))
	if opt==1:
		data=int(input("enter data to push"))
		st.append(data)
	elif opt==2:
		if len(st)==0:
			print("stack is empty")
		else:
			ele=st.pop()
			print("popped element",ele)
	elif opt==3:
		if len(st)==0:
			print("stack is empty")
		else:
			ele=st[-1]
			print("topmost element",ele)
	elif opt==4:
		print(st)
	elif opt==5:
		break
	else:
		print("invalid opt")