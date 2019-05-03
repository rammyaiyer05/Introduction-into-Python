#wapp to find whether the year is leap or not. Year is given from cmd line

year=int(input("Enter the year:"))

if((year % 100!=0 and year%4==0) or (year%100==0 and year%400==0)):
	print("It is a leap year")
else:
	print("It is not a leap year")