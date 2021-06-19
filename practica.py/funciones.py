def calcular_total(num1, num2, num3):
    return num1 + num2 + num3
    #return return


def promedio():
    numero_1 = float(input('primer numero: '))
    numero_2 = float(input('segundo numero: '))
    numero_3 = float(input('tercer numero: '))
    return  calcular_total(numero_1, numero_2, numero_3) / 3
    #return total / 3

print(promedio())
