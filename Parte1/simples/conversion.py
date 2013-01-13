
inch_in_cm = 2.54
longitud = float(raw_input('Ingrese longitud: '))
pulg_equiv = longitud / inch_in_cm
print str(longitud) + 'cm = ' + str(round(pulg_equiv, 4)) + 'in'
