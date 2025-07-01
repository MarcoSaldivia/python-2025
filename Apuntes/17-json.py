import json   # Manipulacion de archivos json
import os     # Metodos para trabajar con el SO


ruta = os.pach.join("json-2025", "datos.jason") # Ruta relativa


# LECTURA DE ARCHIVO JSON
print(""""LECTURA DE ARCHIVO JSON""")
# La letra "r" es de read
# utf-8 es el encoding para trabajar en idioma español

with open(ruta, "r", encoding="utf-8") as archivo:   
    datos = json.load(archivo) # Conversion JSON a estructura Python

# Mostrar los usuarios del archivo JSON
for usuario in datos:
    print(f"ID: {usuario['ID']}, Nombre: {usuario['Nombre']}, Edad: {usuario['Edad']}")


# ESCRITURA DE ARCHIVO JSON
print(""""ESCRITURA DE ARCHIVO JSON""")

# Creando un nuevo usuario
nuevo_usuario = {
    "id" : 5,
    "nombre" : "Fernanda",
    "edad" : 30
}

datos.append(nuevo_usuario)

# Guardar los cambios en el archivo JSON utilizando json.dump()
# w = write = escribir
with open(ruta, "w", encoding="utf-8") as archivo:   
    datos = json.dump(
        datos,
        archivo,
        indent=4
    )
