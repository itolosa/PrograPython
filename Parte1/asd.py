
'''
Saludo

Escriba un programa que pida al usuario que escriba su nombre, y lo salude llamándolo por su nombre.

Ingrese su nombre: Perico
Hola, Perico

'''

nombre = raw_input('Ingrese su nombre: ')
print 'Hola, ', nombre

'''
Círculos

Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

Ingrese el radio: 5
Perimetro: 31.4
Área: 78.5

'''
from math import pi
radio = float(raw_input('Ingrese el radio: '))
perimetro = 2.0 * pi * radio
area = pi * (radio ** 2)
print 'Perimetro:', perimetro
print u'Área:', area

'''

Promedio

Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

Primera nota: 55
Segunda nota: 71
Tercera nota: 46
Cuarta nota: 87
El promedio es: 64.75
'''

nota1 = float(raw_input('Primera nota: '))
nota2 = float(raw_input('Segunda nota: '))
nota3 = float(raw_input('Tercera nota: '))
nota4 = float(raw_input('Cuarta nota: '))
promedio = (nota1 + nota2 + nota3 + nota4) / 4.0
print 'El promedio es:', round(promedio, 2)

'''

Conversión de unidades de longitud

Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

Ingrese longitud: 45
45 cm = 17.7165 in

Ingrese longitud: 13
13 cm = 5.1181 in

'''
inch_in_cm = 2.54
longitud = float(raw_input('Ingrese longitud: '))
pulg_equiv = longitud / inch_in_cm
print str(longitud) + 'cm = ' + str(round(pulg_equiv, 4)) + 'in'

'''
Número invertido

Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

Ingrese numero: 345
543

Ingrese numero: 241
142

'''

num_normal = int(raw_input('Ingrese numero: '))
d1 = (num_normal % 10)
d2 = (num_normal % 100) / 10
d3 = num_normal / 100
num_invertido = d1*100 + d2*10 + d3
print num_invertido

'''

Pitágoras

Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.

Ingrese cateto a: 7
Ingrese cateto b: 5
La hipotenusa es 8.6023252670426267

'''
from math import sqrt
a = float('Ingrese cateto a: ')
b = float('Ingrese cateto b: ')
c = sqrt((a ** 2) + (b ** 2))
print 'La hipotenusa es', c

'''

Hora futura

Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

Hora actual: 3
Cantidad de horas: 5
En 5 horas, el reloj marcara las 8

Hora actual: 11
Cantidad de horas: 43
En 43 horas, el reloj marcara las 6

'''

t = int(raw_input('Hora actual: '))
h = int(raw_input('Cantidad de horas: '))
h_futura = (t + h) % 12
print 'En', h, 'horas, el reloj marcara las', h_futura

'''

Parte decimal

Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

Ingrese un numero: 4.5
0.5

Ingrese un numero: -1.19
0.19

'''

num = abs(float(raw_input('Ingrese un numero: ')))
decimal = num - int(num)
print decimal

'''

Qué nota necesito

Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

El promedio del ramo se calcula con la siguiente formula.
NC=(C1+C2+C3)3
NF=NC⋅0.7+NL⋅0.3

Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final.

Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

Ingrese nota certamen 1: 45
Ingrese nota certamen 2: 55
Ingrese nota laboratorio: 65
Necesita nota 72 en el certamen 3

'''

nota_minima = 55
c1 = float(raw_input('Ingrese nota certamen 1: '))
c2 = float(raw_input('Ingrese nota certamen 2: '))
lab = float(raw_input('Ingrese nota laboratorio: '))
nota_necesaria = int(round((3.0 * (nota_minima - lab)) - c1 - c2, 0))
print 'Necesita nota', nota_necesaria, 'en el certamen 3'

'''
Huevos a la copa
'''

from math import pi, ln
#masas
M_peq = 47.0 #para un huevo pequeño
M_grande = 67.0 #para uno grande,

##constantes
ro = 1.038
c = 3.7
K = 5.4E-3 
To = float(raw_input('Ingrese temp. original del huevo: '))
Tw = 100.0 #temp ebullicion H2O
Ty = 70.0 #temp yema maxima

##tiempo en segundos (decimal)
t = (  ( (M_peq ** (2.0/3.0)) * c * (ro ** (1.0/3.0)) ) / ( K * (pi ** 2.0) * (((4.0/3.0) * pi) ** (2.0/3.0)) )  ) * ln(0.76 * ((To - Tw) / (Ty - Tw)))
print 'Tiempo necesario:', int(round(t, 0)), 'segundos'


#######ESTRUCTURAS CONDICIONALES###############
'''
Determinar par

Escriba un programa que determine si el número entero ingresado por el usuario es par o no.

Ingrese un número: 4
Su número es par

Ingrese un número: 3
Su número es impar
'''

numero = int(raw_input(u'Ingrese un número: '))
print u'Su número es', 'impar' if numero % 2 else 'par'

'''

Años bisiestos

Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido exactamente 365 rotaciones sobre sí misma, sino un poco más. Más precisamente, la diferencia es de más o menos un cuarto de día.

Para evitar que las estaciones se desfasen con el calendario, el calendario juliano introdujo la regla de introducir un día adicional en los años divisibles por 4 (llamados bisiestos), para tomar en consideración los cuatro cuartos de día acumulados.

Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente 3/400 de día.

Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo calendario, en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que fuera divisible por 400.

Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:

Ingrese un anno: 1988
1988 es bisiesto

Ingrese un anno: 2011
2011 no es bisiesto

Ingrese un anno: 1700
1700 no es bisiesto

Ingrese un anno: 1500
1500 es bisiesto

Ingrese un anno: 2400
2400 es bisiesto

'''

anio = int(raw_input('Ingrese un anno'))
if (anio % 4) and ((anio < 1582) or ((anio % 100 != 0) or (anio % 400 == 0))):
	print anio, 'es bisiesto'
else:
	print anio, 'no es bisiesto'

'''
División

Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

Dividendo: 14
Divisor: 5

La división no es exacta.
Cociente: 2
Resto: 4

Dividendo: 100
Divisor: 10

La división es exacta.
Cociente: 10
Resto: 0
'''

dividendo = int(raw_input('Dividendo: '))
divisor = int(raw_input('Divisor: '))
cociente = dividendo / divisor
resto = dividendo % divisor
print 'La división ' + 'no' if resto else '' + 'es exacta'
print 'Cociente:', cociente
print 'Resto', resto

'''
Palabra más larga

Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

Palabra 1: edificio
Palabra 2: tren
La palabra edificio tiene 4 letras mas que tren.

Palabra 1: sol
Palabra 2: paralelepipedo
La palabra paralelepipedo tiene 11 letras mas que sol

Palabra 1: plancha
Palabra 2: lapices
Las dos palabras tienen el mismo largo
'''

p1 = raw_input('Palabra 1: ')
p2 = raw_input('Palabra 2: ')
diferencia = len(p1) - len(p2)
if diferencia > 0:
	print 'La palabra', p1, 'tiene', diferencia, 'letras mas que', p2
elif diferencia < 0:
	print 'La palabra', p2, 'tiene', diferencia * (-1), 'letras mas que', p1
else:
	print 'Las dos palabras tienen el mismo largo'


'''

Ordenamiento

Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:

Ingrese numero: 51
Ingrese numero: 24
24 51

A continuación, escriba otro programa que haga lo mismo con tres números:

Ingrese numero: 8
Ingrese numero: 1
Ingrese numero: 4
1 4 8

Finalmente, escriba un tercer programa que ordene cuatro números:

Ingrese numero: 7
Ingrese numero: 0
Ingrese numero: 6
Ingrese numero: 1
0 1 6 7

Recuerde que su programa debe entregar la solución correcta para cualquier combinación de números, no sólo para los ejemplos mostrados aquí.

Hay más de una manera de resolver cada ejercicio.
'''

num1 = int(raw_input('Ingrese numero: '))
num2 = int(raw_input('Ingrese numero: '))
if num1 > num2:
	print num1, num2
else:
	print num2, num1

num1 = int(raw_input('Ingrese numero: '))
num2 = int(raw_input('Ingrese numero: '))
num3 = int(raw_input('Ingrese numero: '))

#mejor caso O(2)
#peor caso O(3)

if num1 > num2:
	if num2 > num3:
		print num1, num2, num3
	else:
		if num1 > num3:
			print num1, num3, num2
		else:
			print num3, num1, num2
else:
	if num2 < num3:
		print num3, num2, num1
	else:
		if num1 < num3:
			print num2, num3, num1
		else:
			print num2, num1, num3

num1 = int(raw_input('Ingrese numero: '))
num2 = int(raw_input('Ingrese numero: '))
num3 = int(raw_input('Ingrese numero: '))
num4 = int(raw_input('Ingrese numero: '))

if num1 > num2:
	max1 = num1
	min1 = num2
else:
	max1 = num2
	min1 = num1

if num3 > num4:
	max2 = num3
	min2 = num4
else:
	max2 = num4
	min2 = num3

if max1 > max2:
	maximo = max1
	up_med = max2
else:
	maximo = max2
	up_med = max1

if min2 < min1:
	minimo = min2
	low_med = min1
else:
	minimo = min1
	low_med = min2

print maximo, up_med, low_med, minimo

'''

Letra o número

Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.

Ingrese caracter: 9
Es numero.

Ingrese caracter: A
Es letra mayúscula.

Ingrese caracter: f
Es letra minúscula.

Ingrese caracter: #
No es letra ni número.

'''

caracter = raw_input('Ingrese caracter: ')
if '0' <= caracter <= '9'
	print u'Es número.'
elif 'a' <= caracter <= 'z':
	print u'Es letra minúscula.'
elif 'A' <= caracter <= 'Z':
	print u'Es letra mayúscula.'
else:
	print u'No es letra ni número.'

'''

Calculadora

Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.

El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.

La salida del programa debe ser el resultado de la operación.

Operando: 3
Operador: +
Operando: 2
3 + 2 = 5

Operando: 6
Operador: -
Operando: 7
6 - 7 = -1

Operando: 4
Operador: *
Operando: 5
4 * 5 = 20

Operando: 10
Operador: /
Operando: 4
10 / 4 = 2.5

Operando: -1
Operador: **
Operando: 4
-1 ** 4 = 1

'''
operando1 = str(int(raw_input('Operando: ')))
operador = raw_input('Operador: ')
operando2 = str(int(raw_input('Operando: ')))
if operador in ('*', '**', '/', '+', '-'):
	print operando1 + ' ' + operador + ' ' + operando2 + ' =', eval(operando1 + operador + operando2)

'''

Edad

Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

Ingrese su fecha de nacimiento.
Dia: 14
Mes: 6
Anno: 1948
Usted tiene 62 annos

Por supuesto, el resultado entregado depende del día en que su programa será ejecutado.

Para obtener la fecha actual, puede hacerlo usando la función localtime que viene en el módulo time. Los valores se obtienen de la siguiente manera (suponiendo que hoy es 11 de marzo de 2011):

>>> from time import localtime
>>> t = localtime()
>>> t.tm_mday
11
>>> t.tm_mon
3
>>> t.tm_year
2011

El programa debe tener en cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocurre.
'''
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

'''

Set de tenis

El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. 
En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.

Un partido de tenis se divide en sets. 
Para ganar un set, un jugador debe ganar 6 juegos, 
pero además debe haber ganado por lo menos dos juegos más que su rival. 
Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. 
Si el set está empatado a 6 juegos, el set se define en un último juego, en cuyo caso el resultado final es 7-6.

Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

    si A ganó el set, o
    si B ganó el set, o
    si el set todavía no termina, o
    si el resultado es inválido (por ejemplo, 8-6 o 7-3).

Desarrolle un programa que solucione el problema de Solarrabietas:


'''

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

'''

Triángulos

Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: 
cada uno de los lados no puede ser más largo que la suma de los otros dos.

Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

    si acaso el triángulo es inválido; y
    si no lo es, qué tipo de triángulo es.

Ingrese a: 3.9
Ingrese b: 6.0
Ingrese c: 1.2
No es un triangulo valido.

Ingrese a: 1.9
Ingrese b: 2
Ingrese c: 2
El triangulo es isoceles.

Ingrese a: 3.0
Ingrese b: 5.0
Ingrese c: 4.0
El triangulo es escaleno.

'''

a = float(raw_input('Ingrese a: '))
b = float(raw_input('Ingrese b:	'))
c = float(raw_input('Ingrese c: '))

if a < (b+c) and b < (a+c) and c < (a+b):
	if a == b == c:
		print 'El triangulo es equilatero.'
	elif (a == b) or (b == c) or (a == c):
		print 'El triangulo es isoceles.'
	else:
		print 'El triangulo es escaleno.'
else:
	print 'No es un triangulo valido.'

'''
Índice de masa corporal

Ejercicio sacado de [Camp09].

El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

      	edad < 45 	edad ≥ 45
    IMC < 22.0 	bajo 	medio
    IMC ≥ 22.0 	medio 	alto

El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.

Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.
'''

edad = int(raw_input('Ingrese su edad: '))
peso = float(raw_input('Ingrese su peso: '))
estatura = float(raw_input('Ingrese su estatura: '))
IMC = peso / (estatura ** 2)
if IMC < 22.0:
	riesgo = 'bajo' if edad < 45 else 'medio'
else:
	riesgo = 'medio' if edad < 45 else 'alto'
print 'Condicion de riesgo: ' + riesgo
