p1 = raw_input('Palabra 1: ')
p2 = raw_input('Palabra 2: ')
diferencia = len(p1) - len(p2)
if diferencia > 0:
	print 'La palabra', p1, 'tiene', diferencia, 'letras mas que', p2
elif diferencia < 0:
	print 'La palabra', p2, 'tiene', diferencia * (-1), 'letras mas que', p1
else:
	print 'Las dos palabras tienen el mismo largo'