jug_A = int(raw_input('Juegos ganados por A: '))
jug_B = int(raw_input('Juegos ganados por B: '))

if (jug_A == 7 and 5 <= jug_B < 7) or (jug_A == 6 and (jug_A - jug_B) >= 2):
	print 'Gana A'
elif (jug_B == 7 and 5 <= jug_A < 7) or (jug_B == 6 and (jug_B - jug_A) >= 2):
	print 'Gana B'
elif 0 < jug_A <= 6 and 0 < jug_B <= 6:
	print 'Aun no termina'
else:
	print 'Invalido'