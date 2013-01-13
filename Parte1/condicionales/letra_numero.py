caracter = raw_input('Ingrese caracter: ')
if '0' <= caracter <= '9':
	print 'Es numero.'
elif 'a' <= caracter <= 'z':
	print 'Es letra minuscula.'
elif 'A' <= caracter <= 'Z':
	print 'Es letra mayuscula.'
else:
	print 'No es letra ni numero.'