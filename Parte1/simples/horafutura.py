
t = int(raw_input('Hora actual: '))
h = int(raw_input('Cantidad de horas: '))
h_futura = (t + h) % 12
print 'En', h, 'horas, el reloj marcara las', h_futura
