str1 = str(input("Enter the string"))
new_str=''
for ch in str1:
	if ch == 'a':
		new_str += '$'
	else:
		new_str += ch
print(new_str)



#str1=str1.replace('a','$')
#print(str1)