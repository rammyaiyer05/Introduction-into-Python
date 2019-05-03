#wapp to convert farhrenheit into celcius which would be supplied from command line

print("Enter the temperature in Farhrenheit:")
import sys
fah=float(sys.argv[1])

def c():
	c=(fah-32)/1.8
	print("celcius",c)
	print("celcius %5.2f"%c)
	print("celcius %7.2f"%c)
c()

