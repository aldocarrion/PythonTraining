# for letra in "Hola":
#     print(letra)
# else:
#     print("End ciclo FOR")

# for letra in "Holanda":
#     if letra == "a":
#         print(letra)
#         break  # Para que este proceso solo ocurra la primera vez que se cumpla la condicion
#     else:
#         print(letra)
# else:
#     print("Fin del Ciclo")


# # Imprimir solo numeros pares
# for i in range(6):
#     if i % 2 == 0:
#         print(i)

for i in range(6):
    if i % 2 != 0:
        continue  # continua con la siguiente iteracion
    print(i)
