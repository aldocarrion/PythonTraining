from numeros_identicos import NumerosIdenticosException

resultado = None

try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    if a == b:
        raise NumerosIdenticosException("Ocurrio un error\nNumeros identicos")

    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrio un error: ", e)
    print(type(e))
except TypeError as e:
    print("Ocurrio un error: ", e)
    print(type(e))
except Exception as e:
    print("Ocurrio un error: ", e)
    print(type(e))
else:
    print("No hubieron excepciones xd")
finally:
    print("\nEsto siempre se ejecuta\nFinally, al entrar en try\n")

print("Resultado: ", resultado)
print("Continuamos...")
