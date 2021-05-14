# diccionario compuesto por key y value          a = {   "key" : "Value value value...", ...    }
diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}

print(diccionario)


print(len(diccionario))

print(diccionario["IDE"])  # acceder al valor asociado a la llave
print(diccionario.get("IDE"))

diccionario["IDE"] = "Integrated development enviroment"

print(diccionario)

for termino in diccionario:
    print(termino)

for termino in diccionario:
    print(diccionario[termino])

for valor in diccionario.values():
    print(valor)

# comprobar existencia de un elemento
print("IDE" in diccionario)

# agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

# remover elementos
diccionario.pop("DBMS")
print(diccionario)

# limpiar diccionario
diccionario.clear()
print(diccionario)

# eliminar diccionario
del diccionario
print(diccionario)
