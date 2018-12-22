# 6! = 1 * 2 * 3 * 4 * 5 * 6


a = 6
f = 1
while a > 0:
	f = f*a
	a = a-1
else:
	print("Hey, while's done")
print(f)