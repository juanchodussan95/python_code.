def calcular_tiempo_bus(pasajeros_que_suben, pasajeros_que_bajan):
    recorrido = 90
    tiempo_recorrido_hora = 30
    tiempo_total_minutos = (90 / 30) * 60
    tiempo_paradas = pasajeros_que_suben * 2 + pasajeros_que_bajan * 1
    return tiempo_total_minutos + tiempo_paradas
recojidos = int(input('Numeros de pasajeros recojidos: '))
bajados= int(input('Numeros de pasajeros bajados: '))
print('tiempo que se demora el bus es: ', str (calcular_tiempo_bus(recojidos,bajados)))
    