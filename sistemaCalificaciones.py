print("Sistema de Calificaciones")
valor = int(input("Proporciona un valor entre 0 y 10 : "))

if valor > 0 and valor < 6:
    print("F")
elif valor >= 6 and valor < 7:
    print("D")
elif valor >= 7 and valor < 8:
    print("C")
elif valor >= 8 and valor < 9:
    print("B")
elif valor >= 9 and valor <= 10:
    print("A")
else:
    print("Error de valor.")
