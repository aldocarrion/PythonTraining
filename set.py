# set es una coleccion sin orden ni indices, tampoco tienen elementos repetidos.
# Elementos no se pueden modificar, pero si agregar nuevos o eliminar

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

# largo de un set
print(len(planetas))

# revisar si un elemento esta presente
print("Marte" in planetas)
# revisar si un elemento esta presente
print("Tierra" in planetas)
# agregar elementos al set
planetas.add("Tierra")  # No se puede agregar elementos duplicados
print(planetas)

# eliminar
planetas.remove("Tierra")  # Si no encuentra el elemento, arroja excepcion
print(planetas)

planetas.discard("Jupiters")  # Si no encuentra el elemento, sigue de largo
print(planetas)

planetas.clear()  # remueve todos los elementos del set
print(planetas)

del planetas  # set eliminado
