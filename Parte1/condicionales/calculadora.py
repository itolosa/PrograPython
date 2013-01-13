operando1 = str(int(raw_input('Operando: ')))
operador = raw_input('Operador: ')
operando2 = str(int(raw_input('Operando: ')))
if operador in ('*', '**', '/', '+', '-'):
	print operando1 + ' ' + operador + ' ' + operando2 + ' =', eval(operando1 + operador + operando2)