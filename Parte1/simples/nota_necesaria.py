
nota_minima = 55
c1 = float(raw_input('Ingrese nota certamen 1: '))
c2 = float(raw_input('Ingrese nota certamen 2: '))
lab = float(raw_input('Ingrese nota laboratorio: '))
nota_necesaria = int(round((3.0 * (nota_minima - lab)) - c1 - c2, 0))
print 'Necesita nota', nota_necesaria, 'en el certamen 3'
