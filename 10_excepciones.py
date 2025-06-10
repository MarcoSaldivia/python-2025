entrada = input("Ingrese un valor entero: ") # Valor ingresado es un str

try:
    numero = int(entrada)
    print(f"Numero ingresado: {numero}")
except ValueError:                  # Error por tipo de dato
    print("Error de valor: el valor ingresado no es entero")
except Exception as e:              # Errores genericos e inesperados
    print(f"Error inesperado: {e}")
else:
    print("Conversion fue exitosa")
finally:
    print("Finalizacion del bloque")


# Exception = Superclass
##### Subdivisiones de exception
# ValueError (Error especifico)
# ZeroException (Error especifico cuando 2/0)
# FileNotFoundError (Error cuando un archivo no existe)
