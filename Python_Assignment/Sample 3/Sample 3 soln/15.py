l=input("Enter the elements of list")
size=int(input("Enter the size to split the group"))

def group(l,size):
	list1=[]
	while(len(l)>size):
		list1.append(l[:size])
		l=l[size:]
	else:
		list1.append(l)
		return list1

list_group=group(l,size)
for i in list_group:
	print(i)
