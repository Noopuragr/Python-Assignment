import sys
fname=sys.argv[1]
infile = open(fname, 'r')
sum=0
#print infile.read()
filelines=infile.readlines()
for n in filelines:
	print(n)
	sum=int(n)+sum
print(sum)
#priprint#list=filelines.split()
#print(list)
#for n in filelines:
#	sum=sum+n
#print(sum)
