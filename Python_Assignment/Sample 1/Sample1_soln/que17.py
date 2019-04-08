str1 = str(input("Enter the string"))
count = 0
for ch in str1:
	if (ch == 'a' or ch =='e' or ch =='i' or ch == 'o' or ch =='u'):
		count = count+1
print(count)