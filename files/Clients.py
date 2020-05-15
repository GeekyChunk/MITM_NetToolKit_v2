
from socket import *
ip = raw_input('Enter The IP Class: ')
print
n=0
for i in range(1,255):
	try:
		live = gethostbyaddr(ip+str(i)) # 192.168.1.i
		print "IP Live: ",ip+str(i)," ",Live
	except:
            n+=1
            if n == 2:
                break
		print "-------"