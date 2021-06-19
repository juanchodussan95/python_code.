edad = 12

#if edad >= 18:
#    print('Es mayor de edad')
#else:
#    print('Es menor de edad')
rango_de_edad = input('Escriba la edad entre los 10 y 45 para saber tu categoria: ')

if rango_de_edad >= '10' and rango_de_edad <= '14' :
    print('infantil')
elif rango_de_edad >= '15' and rango_de_edad <= '17' :
    print('juvenil')
elif rango_de_edad >= '18' and  rango_de_edad < '20' :
    print('sub_20')
elif rango_de_edad >= '20' and rango_de_edad <= '45' :
    print('profecional')

else:
    print('categoria incorecta')


