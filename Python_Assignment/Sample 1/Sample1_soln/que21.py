str1 = str(input("Enter the string"))
count1=0
count2=0
for ch in str1:
	if(ch.isupper()):
		count1= count1+1
	else:
		count2= count2+1
print("The number of upper case is", count1)
print("The number of lowercase is", count2)