str1 = str(input("Enter the string"))
count = 0
count2 = 0
for ch in str1:
	if ch.isdigit():
		count = count+1
	else:
		count2=count2+1
print("The number of digit is", count)
print("THe number of alphabet is", count2)