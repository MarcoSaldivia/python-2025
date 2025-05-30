# CREANDO UNA TUPLA
estudiantes = ('Samir', 'Hector', 'Matias', 'Pia', 'Carlos')

# CREANDO OTRA TUPLA (CON DATOS ESTRUCTURADOS)
tuplita = ([1,2,3,4,5],('Santiago','Viña'), {'Manzana', 'Piña'})

# IMPRIMIENDO UNA TUPLA
print(estudiantes)

# ELIMINANDO EL ULTIMO ELEMENTO DE LA TUPLA (No se puede --> immutables)
""""estudiantes.pop()
print(estudiantes)"""
"""estudiantes = ('Constanza')
print(estudiantes)"""

# FUNCION INDEX EN TUPLAS
print(estudiantes.index('Carlos'))

# METODO SORTED EN TUPLAS (ORDENA ELEMENTOS Y LO PASA A LISTA)
print(sorted(estudiantes))
