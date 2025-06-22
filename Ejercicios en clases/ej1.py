# 1. Crear un algoritmo que sirva de Conversor de Temperatura:

# PEDIR UN NUMERO DE GRADOS CELSIUS
celsius = int(input("Ingrese la temperatura en grados Celsius: "))

# CALCULOS
fahrenheir = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# RESULTADOS
print(f"La temperatura en grados Celsius es: {celsius}"), round(celsius,(2))
print(f"La temperatura en grados Fahrenheir es: {fahrenheir}"), round(fahrenheir,(2))
print(f"La temperatura en grados Kelvin es: {kelvin}"), round(kelvin,(2))
