try:
    archivo = open("prueba.txt", "r")
    # C:\\Users\\Aldo\\Python-Udemy\\Fundamentos\\prueba.txt rutas con doble \\
    # print(archivo.read())

    # print(archivo.readline())
    # print(archivo.readline())

    # for linea in archivo:
    #     print(linea)

    # print(archivo.readlines())

    # print(archivo.readlines()[2])

    # con a se anexa informacion al archivo
    archivo2 = open("copia.txt", "w")
    archivo2.write(archivo.read())

except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
