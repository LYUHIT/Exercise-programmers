def selfnum ():
	num=[]
	for k in range(10000):
		num.append(False)
	for i in range(10000):
		n = i+(i%10)+((i%100)//10)+((i%1000)//100)+((i%10000)//1000)
		if(n<10000):
			num[n] = True
	for j in range(10000):
		if num[j]==False :
			print(j)	
selfnum()