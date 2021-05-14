nombres = ["Juan", "Karla", "Ricardo", "Maria"]
print(nombres)
print(len(nombres))  # cantidad de elementos en la lista
# Sin incluir indice 2 / imprime elementos desde el inicio dado hasta el incide dado
print(nombres[0:2])
# Sin incluir indice 3 / imprime elementos desde el inicio hasta el incide dado
print(nombres[:3])
# Imprime los elementos desde el indice indicado hasta el final de la lista
print(nombres[1:])
# reemplaza en la lista el elemento indicado por el elemento dado en el indice indicado
nombres[3] = "Ivonne"

for nombre in nombres:
    print(nombre)

if "Karla" in nombres:
    print("Karla si existe")
else:
    print("No existe")

nombres.append("Lorenzo")  # agrega ekemento al final de la lista
print(nombres)

nombres.insert(1, "Javier")  # agrega elemento en indice indicado
print(nombres)

# Elimina la primera instancia del elemento en funcion
nombres.remove("Javier")
print(nombres)

nombres.pop()  # Elimina el ultimo elemento de la lista
print(nombres)

# Elimina un elemento indicando el indice / remueve la variable sin []
del nombres[0]
print(nombres)

nombres.clear()  # Vacia la lista
print(nombres)

del nombres

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)
for i in numeros:
    if i % 3 == 0:
        print(i)
