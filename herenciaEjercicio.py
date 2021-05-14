class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Vehiculo:" + "\nColor: " + self.color + "\nRuedas: " + str(self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + "\nVelocidad: " + str(self.velocidad) + "km/h"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + "\nTipo: " + str(self.tipo)


vehiculo = Vehiculo("Azul", 4)
print(vehiculo)

coche = Coche("Azul", 4, 100)
print(coche)

bici = Bicicleta("Rojo", 2, "urbana")
print(bici)
