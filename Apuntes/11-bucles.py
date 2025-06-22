# While (mientras)
num = 11
while num < 100:
    print(num)
    num += 2

# While (infinito)
while True:
    print(num)
    num += 2
# Control + C para finalizarlo

#01-white
edad = 15
num = 0

# Bucle infinito
''''while edad <18:
    print("Eres menor de edad, no puedes manejar")'''''
# Mal hecho, Falta un else


# While (if/else)
while num < 100:
    print(num)
    num += 2
else: 
    print("Mi condicion es igual o mayor a 100")

# Uso del break
while true:
    parametro = input(">")
    if parametro == "salir":
            break
    else:
        print(parametro)


# Uso del continue
num = 0

while num < 50:
    num += 1 # de 1 en 1
    if num == 40:
        continue
    print(num)



# FOR ##SE OCUPA MUCHO PARA LISTAS O DICCIONARIOS
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista:
    print(i)

# Funcion Range
for i in range(1,10):
    print(i)

# Controles avanzados
# BUCLES ANIDADOS Y BUENAS PRÁCTICAS (BUCLES DENTRO DE OTRO BUCLE)

for n in range(2,10):
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} es un numero compuesto, divisible por {i}")
            break
    else:
        print(f"{n} es un numero primo")


# Bucles anidados
# Ejemplo matriz

matriz = [
    [1, 2, 3],  # Fila 0
    [4, 5, 6],  # Fila 1
    [7, 8, 9]   # Fila 2
]  #c0 #c1 #c2

for fila_id, fila in enumerate(matriz):
    for col_id, valor in enumerate(file):
        print(f"Posicion ({fila_id}, {col_id} = {valor})")


# TÉCNICAS PARA SALIR DE BUCLES ANIDADOS
# Patron bandera
encontrado = False
for fila in matriz :
    for val in fila:
        if val == 5:
            encontrado = True
            print("Valor encontrado:", val)
            break
    if encontrado:
        break
