class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    # Metodo sobreescrito de la clase padre object

    def __add__(self, otro):
        return self.__nombre + " " + otro.__nombre

    def __sub__(self, otro):
        return "Operacion no soportada"


p1 = Persona("Juan")
p2 = Persona("Javiera")

# una nueva forma de trabajar ( Funcionalidad ) al operador + ( sobrecarga )
print(p1 + p2)

print(p1 - p2)


# __add__(self, other)  ==> +
# __sub__(self, other)  ==> -
# __mul__(self, other)  ==> *
# __truediv__(self, other)  ==> /
# __floordiv__(self, other)  ==> //
# __mod__(self, other)  ==> %
# __pow__(self, other)  ==> **

# Buscar Operators / Magic Method / Sobrecarga de operadores
