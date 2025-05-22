def calcular_promedio(lista):
    assert len(lista) > 0, "La lista esta vacia"
    return sum(lista) / len (lista)

#promedio =calcular_promedio([5,5,5])

#print(promedio)

try:
    promedio=calcular_promedio(lista=[5,5])
    print("el promedio es: ",promedio)
except AssertionError as assert_error:
    print(assert_error)
except Exception as e:
    print("la funcion no se calculo correctamente")
    print(e)