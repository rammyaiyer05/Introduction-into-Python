#wapp to read marks from user and give the grade
#A marks>90,B>75,C>60 else D

mar=int(input("enter your marks"))

if(mar>90):
	print("Grade A")
elif(mar>75):
	print("Grade B")
elif(mar>60):
	print("Grade C")
else:
	print("Grade D")