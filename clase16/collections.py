palabra = 'una palabra'
print(palabra)
lista = list(palabra)
print(lista)
diccionario = {'nombre':'lina','apellido':'silva'}
lista = list(diccionario.keys())
lista = list(diccionario.values())
#lista = list(diccionario.items())
print(lista)
tupla = tuple(lista)
print(tupla)
lista = list(palabra)
palabra = ''.join(lista)
print(palabra)