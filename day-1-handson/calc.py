num1 = 19
num2 = 34

ops = ['+', '-', '/','*','**','%']

for op in ops:
	print(eval(str(num1)+op+str(num2)))
