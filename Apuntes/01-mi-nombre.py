nombre = "Marco"
apellido = "Saldivia"

# UTILIZANDO VARIABLES EN UN PRINT CON COMAS
print("Hola mi nombre es:", nombre, "y mi apellido es:", apellido )

# IMPRIMIENDO CON OPERADOR DE CONCATENACION
print("Hola mi nombre es: " + nombre + " y mi apellido es: " + apellido )

# IMPRIMIENDO CON F-STRINGS(CADENAS LITERALES)
print(f"Hola mi nombre es {nombre} y mi apellido es {apellido}")

# INICIALIZANDO MULTI VARIABLES EN UNA SOLA LINEA (NO RECOMENDADO)
ciudad, region, pais = "Castro", "Los Lagos", "Chile"
print(f"Hola soy de {ciudad}, {region}, {pais}")

# USO DEL INPUT / MUTABILIDAD
print(nombre)
nombre = input("Ingrese su nombre:")
print(f"Hola mi nombre es: (nombre)") 

print(nombre)