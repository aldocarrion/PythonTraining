class Persona:  # Automaticamente hereda de la clase "object"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # super() permite acceder a los metodos de la clase padre.
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return super().__str__() + ", sueldo: " + str(self.sueldo)


persona = Persona("Juan", 28)
print(persona)

empleado = Empleado("Karla", 30, 500000)
print(empleado)

empleado.nombre = "Karla Ivonne"
empleado.sueldo = 1000000
print(empleado)
