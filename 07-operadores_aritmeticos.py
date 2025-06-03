
# and = funcion logica "Y"
# or = funcion logica "o"
# not = funcion logica "no"

# Tabla de verdad / Operador or
# False + False = False
# False + True = False
# True + False = False
# True + True = True

# Declarando variables de tipo entero
a = 10
b = 5
c = 4
d = 10

# Operaciones comunes
print(f"Resta entre a - b es: {a - b}")
print()


# Declarando variables de tipo flotantes
t = 5.39 # Tiempo de segundos
g = 9.81 # L a aceleracion de la gravedad

# Operaciones aritmeticas
v = g * t # Formula de caida libre

print(F"La velocidad del objeto en caida libre es de {v} m/s")

# Declarando variables de tipo complejo
c1 = 4 + 3j
print(type(c1))

# Creando un numero complejo con complex
c2 = complex(3, -5)

print("El numero complejo es:",c2)

print(c2.real) # Obteniendo la parte real del numero complejo
print(c2.imag) # Obteniendo la parte imaginaria del numero complejo

# Operadores de comparacion
print(a == b) # Igual a
print(a != b) # Desigual a
print(a > b) # Mayor que
print(a < b) # Menor que
print(c >= d) # Mayor o igual a
print(c <= d) # Menor o igual a 
