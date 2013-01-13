dividendo = int(raw_input('Dividendo: '))
divisor = int(raw_input('Divisor: '))
cociente = dividendo / divisor
resto = dividendo % divisor
print 'La division' + (' no ' if resto else ' ') + 'es exacta'
print 'Cociente:', cociente
print 'Resto', resto
