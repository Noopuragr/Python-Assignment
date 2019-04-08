import os
import sys
def checkSize():
	a=sys.argv[1]
	b=sys.argv[2]
	c=int(b)
	d=sys.argv[3]
	if d=='K':
		#print(c)
		return(c)
	elif d=='M':
		c=c*1024
		#print(c)
		return(c)
	elif d=='G':
		c=c*1024*1024
		return(c)
def largeFile():	
	lof=[f for f in os.listdir() if os.path.isfile(f)]
	for i in lof:
		x=os.path.abspath(i)
		l=os.path.getsize(x)
		m=int(l)
#		print(int(checkSize()))
#		print(m)
		if m>int(checkSize()):
			print(os.path.abspath(i))
checkSize()
largeFile()