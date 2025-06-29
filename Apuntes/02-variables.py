
estatura = 1.80
peso = 105
complejo = 2 + 9j # Inicializando un numero complejo
complejo2 = complex(1, 4) # Otra forma de inicializar un numero complejo

# IMPRESION DE NUMEROS COMPLEJOS
print(complejo)
print(complejo2)

# OPERACION ARITMETICA
imc = peso / (estatura ** 2)
print(f"Su IMC es: {imc}")

# FORMATO DE SALIDA DEL RESULTADO (UTILIZANDO EL METODO FORMAT)
print("Su IMC es: {:,2f}", format(imc))

# FORMATO DE SALIDA DEL RESULTADO (UTILIZANDO F-STRINGS Y :.2F)
print(f"Su IMC es: {imc:.2f}") #Salida con 2 decimales




# DATOS DE TIPO STRING (CADENAS DE TEXTO)
carrera = 'Ingenieria Civil en Informatica'
asignatura = "Programacion"
descripcion = '''Esta es una asignatura de primer semestre'''

# IMPRESION DE CARACTERES EN UNA CADENA DE TEXTO
print(carrera[0]) # Imprime el primer caracter de la cadena
print(carrera[-1]) # Imprime el ultimo caracter de la cadena




print("Hola" * 4)
# print("Hola"/2)

# UTILIZANDO EL INTERVALO DE UNA CADENA
print(asignatura[0:6])

# APLICANDO EL METODO SPLIT (GENERA ARREGLO DE CADENAS)
print(description.split())

# ARREGLO NUMERICO
v = [1, 2, 3, 4, 5] # Inicializando un arreglo numerico 
print(v[0]) # El valor de cero marca la posicion del primer elemento (indice)


# FUNCION LEN
print(f'La palabra {carrera} tiene {len(carrera)} letras.')


# VALORES BOOLEANOS
interruptor = True 
ampolleta = False

print(interruptor, ampolleta)
# FUNCION TYPE PERMITE SABER EL TIPO DE DATO QUE SE UTILIZA
print(type(interruptor))


# COMPARATIVA DE VALORES LOGICOS 
print(1<10)
print(100<=20)
print(100==100)


print(bool("")) # Tiene que haber algo dentro de los () para que me verdadero
print(bool(1)) # Por es "()" y "0" sale falso
print(bool(0))
print(bool("Hola"))

# VARIABLES ROUND, FUNCION QUE ENCAPZULA 
round(celsius,(2))
