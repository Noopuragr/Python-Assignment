import os
import sys
def matchingFiles():
	a=sys.argv[1]
#	print(a)
	b=sys.argv[2]
	lof=[f for f in os.listdir() if os.path.isfile(f)]
	print(lof)
	for i in lof:
		if i==b:
			print("Found")
matchingFiles()