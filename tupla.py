# Tupla mantiene el orden y no se puede modificar

frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)
# largo de tupla
print(len(frutas))
# elemento especifico, navegacion inversa disponible
print(frutas[1])
# rango
print(frutas[0:2])
# modificar un valor
# frutas[0] = "Naranjita" avisa que la tupla no puede ser editada

frutasLista = list(frutas)  # convierte la tupla en una lista

frutasLista[1] = "Platanito"  # Lista modificada

frutas = tuple(frutasLista)  # lista convertida en una tupla

print(frutas)

for fruta in frutas:
    print(fruta, end=", ")

# NO SE PUEDEN AGREGAR O ELIMINAR ELEMENTOS EN UNA TUPLA
del frutas
