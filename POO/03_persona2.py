#crear el plano para crear objetos

class Persona:
    pass

pedro=Persona()
print(type(pedro))

paco=Persona()
print(type(paco))

print(pedro == paco)

class Persona2:
    def __init__(self):
        print("estoy en el constructor")

paco2 = Persona2()

class Persona3:
    atributo=123
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

paco3 = Persona3("paco",20)
print(paco3.nombre)
print(paco3.edad)
print(paco3.atributo)
