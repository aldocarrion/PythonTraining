class MiClase:

    variable_clase = "Variable de Clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


print(MiClase.variable_clase)

objeto1 = MiClase("Variable Instancia 1")

MiClase.variable_instancia = "Modificando Variable de instancia"

print(MiClase.variable_instancia)

print(objeto1.variable_instancia)

print(objeto1.variable_clase)  # acceder a variables de clase desde el objeto

# modificacion de la variable de clase solamente asociada al objeto
objeto1.variable_clase = "Modificando a la variable de clase"
print(objeto1.variable_clase)

objeto2 = MiClase("")
print(objeto2.variable_clase)
print(objeto2.variable_instancia)
