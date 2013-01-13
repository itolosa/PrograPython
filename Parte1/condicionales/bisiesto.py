anio = int(raw_input('Ingrese un anno: '))
if (anio % 4 == 0) and ((anio < 1582) or ((anio % 100 != 0) or (anio % 400 == 0))):
	print anio, 'es bisiesto'
else:
	print anio, 'no es bisiesto'
