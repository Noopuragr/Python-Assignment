import os
import sys

def get_file():
	if len(sys.argv)==3:
		return(sys.argv[1],sys.argv[2])
	else:
		print("type <pattern> <filename>")
		sys.exit()

def open_file(fname):
	try:
		return(open(fname))
	except IOError:
		print("file not found",fname)
		sys.exit()
def file_readlines(f_dis):
	for line in f_dis.readlines():
		print(lines)

def file_close(f_dis):
	return f_dis.readlines()

def test_pattern():
	pattern,fname=get_file()
	f_dis=open_file(fname)
	file_data=f_dis.readlines()
	file_close(f_dis)
	return(match_pattern(pattern,file_data))

def match_pattern(pattern,file_data):
	pattern_list=[]
	for line in file_data:
		if pattern in line:
			pattern_list.append(line)
		return pattern_list

if __name__=="__main__":
	print(test_pattern())

	