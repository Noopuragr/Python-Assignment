def Dup():
	l1=[10,20,54,10,56,80,80]
	l3=[]
	for i in l1:
		if i not in l3:
			l3.append(i)
		else:
			print(i)
Dup()
