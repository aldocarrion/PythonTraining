numero1 = int(input("Proporciona el numero1: "))
numero2 = int(input("Proporciona el numero2: "))
if(numero1 > numero2):
    print("El numero mayor es: ", numero1)
elif(numero2 > numero1):
    print("El numero mayor es: ", numero2)
else:
    print("ERROR")

condicion = False

print("La condicion es verdadera") if condicion else print("Condicion Falsa")
