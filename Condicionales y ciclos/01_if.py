#Las condicionales son estructuras que se usan para decidir que se va a ejecutar. Si se cumple algo, se ejecutara cierta parte del codigo sino sera otra.
a=1
b=1
if b>a:
    print("B es mayor que A")
elif a>b:
    print("A es mayor que B")
else:
    print("A y B son iguales")

'''
Ejercicio:
Escribe un programa que determine si una persona puede entrar a una montaña rusa.
Condición 1: Debe tener al menos 12 años y medir más de 140 cm.
Condición 2: Si no cumple la primera condición, puede entrar si está acompañada por un adulto (usar or).

El programa debe imprimir "Puedes entrar" o "No puedes entrar".
'''
edad = int(input("Ingresa tu edad: "))
altura = int(input("Ingresa tu altura (en cm): "))
adulto = input("¿Estás acompañado/a por un adulto? (sí/no): ").lower() == "sí"

# Verifica las condiciones usando >, and, or
if (edad >= 12 and altura > 140) or adulto:
    print("Puedes entrar")
else:
    print("No puedes entrar")