print("Bienvenido al sistema de ubicacion para zonas publicas wifi") 
nombre_usuario = '51743' # definicion de usuario
contraseña = '34715' # definicion de contraseña
datos_del_usuario = input('Ingrese nombre: ') # se solicita usuario a la persona

if datos_del_usuario == nombre_usuario:   # comparacion de usuario con el del sistema para validar 
    datos_contraseña = input('Ingrese su contraseña: ') # solicitud de contraseña al usuario
    
    if datos_contraseña == contraseña: # comparacion de contraseña con la del sistema para validar
        print('Solucione el captcha')
        Segundo_dato = 5*3 - 7-4
        valor_captcha = 743 + Segundo_dato # el valor del captcha
        captcha = int(input('solucione 743 + 4 =')) # se solicta la solucion del captcha
        
        if valor_captcha == captcha: # se compara el dato ingresado por el usuario y el que esta en el sistema
            print('Sesion Iniciada') # se verifica que el proceso fue correcto
            
        else: 
            print('Error') # hubo algun error en algunos de los procesos solcitados
    else:
        print('Error')
else:
    print('Error')
    