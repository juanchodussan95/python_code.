def verificar_mayor(edad1, edad2, edad3, edad4):
    if edad1 > edad2 > edad3 > edad4:
        print(edad1)
    elif edad2 > edad3 > edad4:
        print(edad2)
    elif edad3 > edad4:
        print(edad3)
    else:
        print(edad4)
verificar_mayor(45,23,48,50)
verificar_mayor(41,43,36,51)
verificar_mayor(34,65,12,68)