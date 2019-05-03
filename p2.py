#wapp to convert farhrenheit into celcius which would be supplied from command line

import sys
fah=float(sys.argv[1])

c=(fah-32)/1.8
print("celcius",c)
print("celcius %5.2f"%c)

