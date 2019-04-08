import os
import sys
def getPath():
	a=sys.argv[1]
	largest_size=0
	largest_file_path=''
	print(a)
	b=os.listdir(a)
	print(b)
	lof=[f for f in os.listdir() if os.path.isfile(f)]
	print(lof)
	for i in lof:
		x=os.path.abspath(i)
		l=os.path.getsize(x)
		if l>largest_size:
			largest_size=l
			largest_file_path=os.path.abspath(i)
	print(largest_size)
	print(largest_file_path)
getPath()