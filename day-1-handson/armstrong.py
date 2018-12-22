## TODO: Do for all numbers.

a = 153
n = len(str(a))
addn = 0
for i in list(str(a)):				# ['1', '5', '3']
	addn = addn + int(i)**n; 

if addn == a:
	print(a, " is Armstrong number")
else:
	print(a, " is not Armstrong number")