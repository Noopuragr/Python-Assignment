import sys
fname=sys.argv[1]
fname2=sys.argv[2]
infile = open(fname, 'r')
copyfile=open(fname2,'w')
for line in infile:
	copyfile.write(line)
