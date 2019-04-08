##Python Program to generate 10 random numbers between 1 to 100 
#such that there should one number between 1 to 10 one number between 11 to 20 etc.

import random
b=10
a=1
for x in range(10):
		if a in range(1,100):
			if b in range(10,100):
				print(random.randint(a,b))
		a=a+10
		b=b+10







	
		

	

 



