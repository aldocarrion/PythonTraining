class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


base = int(input("Ingrese base: "))
altura = int(input("Ingrese altura: "))

rectangulo = Rectangulo(base, altura)

print("Area del rectangulo: ", rectangulo.area())
