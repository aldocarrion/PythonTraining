def mi_funcion():
    print("Ejecutando mi funcion")


mi_funcion()

###################################################################################
# Parametro es una variable definida entre los parentesis de la funcion
# argumento es el valor enviado a la funcion


def funcion_arg(nombre, apellido):
    print("El nombre recibido es: ", nombre)
    print("El apellido recibido es: ", apellido)


funcion_arg("Aldo", "Carrion")


###################################################################################

def suma(a, b):
    return a + b


print("El resultado es: ", suma(5, 3))


def suma(a=0, b=0):
    return a + b


print("El resultado es: ", suma())
