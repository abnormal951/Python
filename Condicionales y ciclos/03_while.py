#El ciclo while ejecuta una o varias instruciones mientras se cumpla la condicion  
i = 1
while i <=5:
    print(i)
    i+=1
    if i == 3:
        break
    

suma = 0


while True:
    numero = int(input("Ingresa un número (o 0 para terminar): "))
    if numero != 0:
        if (numero % 2 ==0):
            suma+= numero 
            
    
    else:
        break
print("la suma de pares es ",suma)   