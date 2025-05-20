# son las estructuras de datos nos permiten guardar otros datos de manera ordenada
# permiten manipulacion, extraccion, busqueda e insercion
# Son eficientes
# Son mutables si sus elementos pueden sen modificados despues de ser creados
'''Existen 4 tipos de estrucruras de datos:
* Listas
* Tuplas
* Diccionarios
* Sets
'''

#Listas: permiten guardar elementos de manera ordenada, son odenadas,
# son mutables, reciben elementos repetidos, se declara con []

print('Listas Ejercicio 1:')
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[0])
print(lista[9])
#lista.insert(5,5)
lista[2] =100
lista.remove(4)
lista.append(20)
print(lista)

print('Listas Ejercicio 2:')
numeros = [3, 8, 12, 5, 9, 10]
lista_pares=[num for num in numeros if num % 2==0]
print(lista_pares)
print(type(lista_pares))

#Tuplas: no son mutables, se declara con ()
print('Tuplas Ejercicio 1:')
tupla = ('lunes','martes','miercoles','jueves','viernes','sabado','domingo')
print(type(tupla))
tupla[2]
tupla=list(tupla)
print(type(tupla))
tupla[2]='miércoles'
tupla=tuple(tupla)
print(type(tupla))
print()

#Diccionarios se declaran con {} y son por acceden a ellos por clave valor

print('Diccionario Ejercicio 1:')
diccionario = {"Juan": 25, "Ana": 30}
print(diccionario)
print(diccionario['Ana'])
diccionario.update({"Luis": 40})
print(diccionario)
del diccionario['Juan']
print(diccionario)

#set se definen con {} y son como las listas.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set3=set1.intersection(set2)
print(set3)