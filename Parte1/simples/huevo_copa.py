from math import pi, log
#masas
M_peq = 47.0 #para un huevo pequenio
M_grande = 67.0 #para uno grande,

##constantes
ro = 1.038
c = 3.7
K = 5.4E-3 
To = float(raw_input('Ingrese temp. original del huevo: '))
Tw = 100.0 #temp ebullicion H2O
Ty = 70.0 #temp yema maxima

##tiempo en segundos (decimal)
t = (  ( (M_peq ** (2.0/3.0)) * c * (ro ** (1.0/3.0)) ) / ( K * (pi ** 2.0) * (((4.0/3.0) * pi) ** (2.0/3.0)) )  ) * log(0.76 * ((To - Tw) / (Ty - Tw)))
print 'Tiempo necesario:', int(round(t, 0)), 'segundos'
