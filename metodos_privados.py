class Persona:
    def __init__(self, nombre, ape_pat, ape_mat):
        self.nombre = nombre  # atributo publico
        # atributo semiprivado puede ser editado fuera de la clase (sin necesidad de get or set)
        self._ape_pat = ape_pat
        self.__ape_mat = ape_mat  # atributo privado

    def metodo_publico(self):
        self.__metodo_privado()

    def __metodo_privado(self):
        print(self.nombre)
        print(self._ape_pat)
        print(self.__ape_mat)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apePat(self):
        return self._ape_pat

    def set_apePat(self, apePat):
        self._ape_pat = apePat

    def get_apeMat(self):
        return self.__ape_mat

    def set_apeMat(self, apeMat):
        self.__ape_mat = apeMat


p1 = Persona("Juan", "Lopez", "Perez")
# p1.__metodo_privado() no se puede acceder ya que es un metodo privado
p1.metodo_publico()

print(p1.nombre)
print(p1._ape_pat)
# print(p1.__ape_mat)
print(p1.get_apeMat())
