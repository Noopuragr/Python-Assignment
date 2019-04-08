import sys
fname=sys.argv[1]
infile = open(fname, 'r')
#print infile.read()
first5lines=infile.readlines()[0:5]
for n in first5lines:
	print(n)
