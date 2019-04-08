def cumulative_list(lists):
	list_var=[]
	length=len(lists)
	list_var=[sum(lists[0:x+1]) for x in range (0,length)]
	return list_var

lists = [10,20,30,40,50]
print(cumulative_list(lists))