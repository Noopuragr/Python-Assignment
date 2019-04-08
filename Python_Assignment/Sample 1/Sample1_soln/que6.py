a=int(input("Enter an integer"))
total=0
while(a>0):
	dig=a%10
	total=total+dig
	a=a//10
print("The sum of digit is ",total)

