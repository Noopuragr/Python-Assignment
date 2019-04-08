num = int(input("Enter the number"))
num2 = num
x=0
while(num>0):
	num1 = num%10
	x=x*10+num1
	num=num//10
if(num2==x):
	print("Palindrome")
else:
	print("Non palindrome")

