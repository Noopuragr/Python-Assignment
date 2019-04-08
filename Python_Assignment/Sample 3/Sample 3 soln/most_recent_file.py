import os
import sys
def getRecentFile():
	a=sys.argv[1]
	print(a)
	b=os.listdir(a)
	lof=[f for f in os.listdir() if os.path.isfile(f)]
#	print(lof)
	latest_file=max(lof,key=os.path.getctime)
	print("The latest file is ",latest_file)
#	print(b)
getRecentFile()

#	latest_file=