#wamdp to implement FIFO/queue

import array
qu=array.array("i",[])

while True:
	opt=int(input("1.insert,2.remove,3.peek,4.display,5.exit"))
	if opt==1:
		data=int(input("enter data to insert"))
		qu.append(data)
	elif opt==2:
		if len(qu)==0:
			print("queue is empty")
		else:
			ele=qu.remove(0)
			print("removed element",ele)
	elif opt==3:
		if len(qu)==0:
			print("queue is empty")
		else:
			ele=qu[0]
			print("first element",ele)
	elif opt==4:
		print(qu)
	elif opt==5:
		break
	else:
		print("invalid opt")