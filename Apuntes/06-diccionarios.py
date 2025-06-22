# CREANDO DICCIONARIO
paciente = {
    'nombre': 'Carlos',
    'apellido': 'Santana',
    'edad': 50,
    'ciudad': 'Puerto Montt',
    'comuna': 'Alerce',  # No es una tupla, es solo una cadena
    'consultas': [14, 20, 40],
    'diagostico': {'Resfrio'},  # Ojo: esto es un conjunto (set), si es solo un string deberías usar una lista o cadena
    'info_extra': {
        'tipo_de_sangre': 'A+',
        'hemograma': 'Sin Datos'
    }
}


# OTRA FORMA DE DECLARAR DICCIONARIO
medico = dict(
    nombre = 'Samir',
    apellido = 'Arana',
    edad = 20,
    especialidaD = 'Neurologo'
)

# IMPRESION DE DICCIONARIOS
print(paciente)
print(medico)

# CONSULTANDO UN ELEMENTO A TRAVES DE LA CLAVE DEL DICCIONARIO
print(medico['nombre'])

# METODO ELIMINANDO UNA CLAVE DEL DICCIONARIO (METODO DEL)
del(paciente['nombre'])
print(paciente)
