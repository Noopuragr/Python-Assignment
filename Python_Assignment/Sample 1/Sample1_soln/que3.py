lower = int(input("Enter the lower range limit"))
upper = int(input("Enter the upper limit"))
n=int(input("Enter the number"))
for i in range(lower,upper+1):
	if(i%n==0):
		print(i)



