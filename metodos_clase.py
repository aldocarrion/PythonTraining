class MiClase:

    variable_clase = "Variable Clase"

    def __init__(self):
        self.variable_instancia = "Variable Instancia"

    # Un metodo estatico no se asocia a los objetos creados por las clases,
    # por lo que no es necesario que reciban parametros

    @staticmethod
    def metodo_estatico():
        print("Metodo estatico")
        print(MiClase.variable_clase)
        # Desde un metodo estatico no podemos acceder a una variable de instancia
        # print(MiClase.variable_instancia)

    # Este metodo si recibe un parametro

    @classmethod
    def metodo_clase(cls):
        print("Metodo de clase: " + str(cls))
        print(cls.variable_clase)
        # No podemos acceder a la variable de instancia desde el contexto estatico
        # print(cls.variable_instancia)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()


MiClase.metodo_estatico()
MiClase.metodo_clase()

print("")
objeto1 = MiClase()
objeto1.metodo_instancia()
