from time import localtime
print 'Ingrese su fecha de nacimiento.'
dia = int(raw_input('Dia: '))
mes = int(raw_input('Mes: '))
anio = int(raw_input('Anno: '))
t = localtime()
if t.tm_year > anio:
	dif_anios = abs(t.tm_year - anio)
	if t.tm_mon < mes or (t.tm_mon == mes and t.tm_mday < dia):
		dif_anios -= 1
	print 'Usted tiene', dif_anios, 'annos'
else:
	print 'Usted tiene 0 annos' #o no ha nacido