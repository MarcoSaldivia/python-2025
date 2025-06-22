#1
nota = float(input("Ingrese su nota (Como decimal): "))

if nota >= 4 and nota < 6.0:
    print("Aprobaste")
elif nota >= 6.0:
    print("Excelente rendimiento!")
else:
    print("Reprobaste")

#2
temperatura = float(input(" Ingrese la temperatura enCelsius: "))

if temperatura < 10: 
    print("Hace frio")
elif temperatura >= 10 and temperatura <= 25:
    print("Clima agradable")
else:
    print("Hace calor")

#3
compra = float(input("Ingrese el monto total de la compra: "))

if compra < 10000:
    descuento = 0
elif compra < 50000:
    descuento = compra * 0.10
else:
    descuento = compra * 0.20

total = compra - descuento
print("Descuento aplicado:", descuento)
print("Total a pagar:", total)

#4
numero_secreto = 7
intento = int(input("Adivina el número (entre 1 y 10): "))

while intento != numero_secreto:
    print("¡Incorrecto! Intenta de nuevo.")
    intento = int(input("Adivina el número (entre 1 y 10): "))

print("¡Felicidades! Adivinaste el número.")

#5
contraseña_correcta = "python123"
contraseña = input("Ingresa la contraseña: ")

while contraseña != contraseña_correcta:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contraseña = input("Ingresa la contraseña: ")

print("¡Acceso concedido!")

#6
edad = int(input("Ingresa tu edad: "))

while edad < 0:
    print("Edad no válida. Intenta de nuevo.")
    edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

numero_secreto = 5
intentos = 0

#7
contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1
else:
    print("El while ha terminado.")

#8 generar numero de 1 a 5
for numero in range(1,6):
    print(numero)

#9 sumar los numeros de 1 al 5
for numero in range(1,6):
    suma += numero
print(f"La suma de los numeros es {suma}")

#10
tabla = int(input("¿De qué número quieres la tabla? "))

for i in range(1, 11):
    resultado = tabla * i
    print(f"{tabla} x {i} = {resultado}")



# Apuntes
# Float (Numero flotante(decimal)) altura = float(input("Ingrese su altura: "))
# int (Un dato a entero) edad= int(input("Escriba su edad")) 
# input (dato) nombre = input("ingrese su nombre: ")
# str (numeros)
