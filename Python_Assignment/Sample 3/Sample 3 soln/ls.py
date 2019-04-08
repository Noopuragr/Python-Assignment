import os
import sys
def getPath():
	if len(sys.argv)==2:
		print(sys.argv[1])
		return(sys.argv[1])
	else:
		print("Enter valid path")
		exit()
arr=os.listdir(getPath())
print(arr)

