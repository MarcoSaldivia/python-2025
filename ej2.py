# 2. Desarrollar un algoritmo con operaciones mixtas con números complejos:

# INGRESAR TRES VALORES
entero = int(input("Ingrese un numero entero: "))
flotante = float(input("Ingrese un numero flotante (decimal): "))
complejo = complex(input("Ingrese un numero complejo (ej: 2+3j): "))

# OPERACIONES
potencia = complejo ** entero
suma_mixta = complejo + flotante
producto_mixto = complejo * entero
modulo = abs(potencia)

# MOSTRAR RESULTADOS
print(f"El resultado de la potencia compleja es: {potencia}")
print(f"El resultado de la suma mixta es: {suma_mixta}")
print(f"El resultado del producto mixto es: {producto_mixto}")
print(f"El modulo de la potencia compleja es {round(modulo, 3)}")
