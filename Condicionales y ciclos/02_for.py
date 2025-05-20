#permite iterar sobre diferentes estructuras de datos e incluso sobre strings iteramos sobre cada elemento de la estructura de datos.
for letra in "texto":
    print(letra)

lenguajes = ['c','c++','java']
for elemento in lenguajes:
    print(elemento)
    
lenguajes = ['c','c++','java']
for elemento in lenguajes:
    if elemento == 'c++':
        continue
    print(elemento)
    
for elemento in range(5):
    print(elemento)
for elemento in range(7,14):
    print(elemento)