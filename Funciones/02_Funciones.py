#Ejemplo 1: Función con parámetros

def sumar(a,b):
    resultado = a+b
    return resultado

total = sumar(8,3)
print(total)

#Ejemplo 3: Función con valor predeterminado
def potencia(numero, exponente=2):
    return numero ** exponente

print(potencia(3))
print(potencia(3,3))

#Ejemplo 4: Función que devuelve múltiples valores
def operaciones(a,b):
    suma = a+b
    resta = a-b
    return suma,resta

resultado_suma,resultado_resta = operaciones(10,5)
print("suma =",resultado_suma)
print("resta =", resultado_resta)

#Ejemplo 5: Función con argumentos variables (*args)

def promedio(*numeros):
    return sum(numeros)/len(numeros)

resultado=promedio(5,10,15)

print(resultado)

#5. Ejercicio Práctico
#Crea una función es_par(numero) 
# que devuelva True si el número es par 
# y False si es impar.

def par_impar (a):
    if a % 2 == 0:
        print("es par")
    else:
        print("Es impar")

res_par_impar =par_impar(10)
    