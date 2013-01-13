
num_normal = int(raw_input('Ingrese numero: '))
d1 = (num_normal % 10)
d2 = (num_normal % 100) / 10
d3 = num_normal / 100
num_invertido = d1*100 + d2*10 + d3
print num_invertido