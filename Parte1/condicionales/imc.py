edad = int(raw_input('Ingrese su edad: '))
peso = float(raw_input('Ingrese su peso: '))
estatura = float(raw_input('Ingrese su estatura: '))
IMC = peso / (estatura ** 2)
if IMC < 22.0:
	riesgo = 'bajo' if edad < 45 else 'medio'
else:
	riesgo = 'medio' if edad < 45 else 'alto'
print 'Condicion de riesgo: ' + riesgo