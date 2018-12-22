for i in range(100):
	flag = False
	for j in range(2, i//2+1):
		if(i%j == 0):
			flag = True
			break
	if(flag == False):
		print(i)