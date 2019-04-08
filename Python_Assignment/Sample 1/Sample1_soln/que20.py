str1 = str(input("Enter the first string"))
str2 = str(input("Enter the second string"))
count1 = 0
count2 = 0
for ch in str1:
	count1 = count1+1
for ch in str2:
	count2 = count2+1
if(count1>count2):
	print(str1)
elif(count2>count1):
	print(str2)
else:
	print("Both string are of same length")
