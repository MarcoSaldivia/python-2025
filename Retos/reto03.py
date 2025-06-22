# Reto 3

num = 500
numeros = []

while num >= 100:
    print(f"Numero: {num}")
    numeros.append(num)
    num -= 3

suma = sum(numeros)
promedio = suma / len(numeros)

print(f"Suma de los numeros: {suma}")
print(f"Promedio de los numeros: {promedio:.2f}")
