a = int(input("Ingrese un valor: "))
valorMin = 0
valorMax = 5
dentroRango = (a >= valorMin and a <= valorMax)
# print(dentroRango)
if(dentroRango):
    print("Dentro del rango")
else:
    print("Fuera de rango")

vacaciones = False
diaDescanso = False
if(vacaciones or diaDescanso):
    print("Podemos ir al parque")
else:
    print("Se deben realizar deberes")
print(not(vacaciones))
