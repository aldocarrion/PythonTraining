class Persona:
    def __init__(self, n, edad):
        # Doble __ significa que el atributo es privado y encapsulado.
        self.__nombre = n
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad


p1 = Persona("Juan", 18)
# print(p1.__nombre)
print(p1.get_nombre())
print(p1.get_edad())

p1.set_edad(45)
p1.set_nombre("Anita")
print(p1.get_nombre())
print(p1.get_edad())
