# 3. Crear un algoritmo que permita manipular cadenas de texto:

# PEDIR/INGRESAR UNA FRASE
frase = str("Ingresa una frase (Maximo 30 caracteres): ")

# CORTAR LA FRASE CUANDO PASE LAS 30 CARACTERES
frase = frase[:30]

print(f"La frase es: {frase}")

# PASAR LA FRASE A MAYUSCULAS Y MINUSCULAS
mayusculas = frase.upper()
minusculas = frase.lower()

# Pasar la frase a minusculas y determinar cuantas "a" o "A" hay en la frase
cantidad_a = frase.lower.count('a')

# MEDIR LA LONGITUD DE LA FRASE
longitud = len(frase)

print(f"La frase tiene {cantidad_a} a.")
print(f"La frase tiene {longitud} letras.")
