class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        return self.operando1 + self.operando2

    def restar(self):
        return self.operando1 - self.operando2

    def multiplicar(self):
        return self.operando1 * self.operando2

    def dividir(self):
        return self.operando1 / self.operando2
# creamos el objeto


aritmetica = Aritmetica(2, 4)


print(aritmetica.sumar())
print(aritmetica.restar())
print(aritmetica.multiplicar())
print(aritmetica.dividir())
