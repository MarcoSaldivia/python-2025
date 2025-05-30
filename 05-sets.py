# CREANDO SETS
colores = {'Azul', 'Rojo', 'Azul', 'Verde'}
colorcitos = {'Azul', 'Naranjo'}

# IMPRIMIENDO EL SET COLORES
print(colores) # Sets no imprime repetidos

# AGREGANDO UN NUEVO ELEMENTO AL SET (METODO ADD)
colores.add('Blanco') # Lo agrega pero su posicion siempre cambiara
print(colores)

# ELIMINANDO UN ELEMENTO DEL SET
colores.discard('Blanco')
print(colores)

# APLICANDO EL METODO DIFFENCE
diferencia = colores.difference(colorcitos)
print(diferencia)
