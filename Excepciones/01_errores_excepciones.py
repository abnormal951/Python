#existen 2 tipos de errores
#De sintaxis: mal escrita la instruccion
#Excepciones: nos generan un error aun sea bien escrita la instruccion ejemplo 7/0
# y ocurren durante la ejecucion del programa

#print"Hola" #error de sintaxis


#exception
def validar_x_(x):
    if x<1:
        raise Exception ("La variables x debe ser mayor a 1")
    else:
        print("La variable x es mayor a 1")

x=1.1
validar_x_(x)