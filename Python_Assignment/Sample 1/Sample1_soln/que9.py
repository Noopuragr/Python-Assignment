num= 1234
x=0
while(num>0):
	dig=num%10
	x=x*10+dig
	num=num//10
print("Reverse of number is",x)
