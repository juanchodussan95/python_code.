num1 =45 
num2 = 56

mensaje = 'los numeros son '+ str(num1) +' , '+ str(num2)
print(mensaje)
mensaje = 'los numeros son {} , {}' . format(num1, num2)
print(mensaje)
mensaje = 'los numeros son {1} , {0} '. format(num1, num2)
print(mensaje)
mensaje = 'los numeros son %d, %d'%(num1, num2)
print(mensaje) 