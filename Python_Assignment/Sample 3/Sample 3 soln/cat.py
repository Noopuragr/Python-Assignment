import sys
fname=sys.argv[1]
#fname = input("Enter the name of the file in "":")
infile = open(fname, 'r')
print(infile.read())
infile.close()