class Persona:
    # asterisco indica que el parametro es opcional. doble asterisco es para hacer ingreso opcional de un diccionario?
    def __init__(this, n, e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d

    def desplegar(this):
        print("Nombre: ", this.nombre)
        print("Edad: ", this.edad)
        print("Valores (Tupla): ", this.valores)
        print("Diccionario: ", this.diccionario)


p1 = Persona("Juan", 28)

p1.desplegar()
print()


p2 = Persona("Esteban", 28, 2, 3, 4, 5)

p2.desplegar()
print()

p3 = Persona("Julia", 40, 2, 3, 6, 9, m="manzana", p="pera")

p3.desplegar()
print()
