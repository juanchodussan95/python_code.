edad = 67 
genero = 'M'
semanas = 260 

if genero == 'M':
    if edad >= 68:
        if semanas >= 279:
            print('se puede pensionar')
        else:
            print('le faltan '+ str(279 - semanas) + ' semanas ')
    else:
        print('le faltan'+ str(68 - edad) + ' años ')
else:
    print('genero invalido ' + str('M' != genero) )