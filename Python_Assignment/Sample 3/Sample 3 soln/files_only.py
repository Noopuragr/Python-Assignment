import os
import sys
def filesOnly():
	a=sys.argv[1]
	print(a)
	b=os.listdir(a)
	lof=[f for f in os.listdir() if os.path.isfile(f)]
	print(lof)
filesOnly()