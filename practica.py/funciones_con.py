def verificar_mayor(edad1, edad2, edad3, edad4):
    if edad1 >= edad2 >= edad3  >= edad4:
        print('1 ' + str(edad1))
    if edad2 > edad3 > edad4 :
        print('2 ' + str(edad2))
    if edad3 > edad4 :
        print('3 ' + str(edad3))
    else:
        print('4 ' + str(edad4))

verificar_mayor(15, 56, 45, 56)
verificar_mayor(12, 90, 64, 90)
     