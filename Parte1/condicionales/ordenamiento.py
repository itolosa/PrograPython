num1 = int(raw_input('Ingrese numero: '))
num2 = int(raw_input('Ingrese numero: '))
if num1 > num2:
	print num1, num2
else:
	print num2, num1

num1 = int(raw_input('Ingrese numero: '))
num2 = int(raw_input('Ingrese numero: '))
num3 = int(raw_input('Ingrese numero: '))

#mejor caso O(2)
#peor caso O(3)

if num1 > num2:
	if num2 > num3:
		print num1, num2, num3
	else:
		if num1 > num3:
			print num1, num3, num2
		else:
			print num3, num1, num2
else:
	if num2 < num3:
		print num3, num2, num1
	else:
		if num1 < num3:
			print num2, num3, num1
		else:
			print num2, num1, num3

num1 = int(raw_input('Ingrese numero: '))
num2 = int(raw_input('Ingrese numero: '))
num3 = int(raw_input('Ingrese numero: '))
num4 = int(raw_input('Ingrese numero: '))

if num1 > num2:
	max1 = num1
	min1 = num2
else:
	max1 = num2
	min1 = num1

if num3 > num4:
	max2 = num3
	min2 = num4
else:
	max2 = num4
	min2 = num3

if max1 > max2:
	maximo = max1
	up_med = max2
else:
	maximo = max2
	up_med = max1

if min2 < min1:
	minimo = min2
	low_med = min1
else:
	minimo = min1
	low_med = min2

print maximo, up_med, low_med, minimo