lista1 = ['Marco', 18, True]
print(lista1)

# LISTA DE NUMEROS
n = [1,2,3,4,5]

# LISTA DE SOLO STRINGS - UTILIZANDO LA FUNCION LIST
ramos = list(['Programacion', 'Quimica', 'POO', 'Programacion'])

# IMPRIME LA POSICION DEL PRIMER ELEMENTO DE LA LISTA (NO EL CARACTER)
print(ramos[0])

# FUNCION COUNT (CUENTA LA CANTIDAD DE CONCURRENCIAS DE UN ELEMENTO)
print(ramos.count('Programacion'))

# FUNCION APPEND (AGREGANDO UN ELEMENTO AL FINAL DE LA LISTA)
ramos.append('Introduccion a la Matematica')
print(ramos)

# MODIFICAR ELEMENTOS A LA LISTA
ramos[1] = "Comunicacion" # Estoy pasando la posicion del elemento modificado
print(ramos)

# OTRA FORMA DE INSERTAR UN ELEMENTO A LA LISTA (INSERT)
ramos.insert(0, 'Algebra')

print(ramos)

# ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA
ramos.pop()
print(ramos)

# ORDENANDO ELEMENTOS DE UNA LISTA 
ramos.sort()
print(ramos)

# ORDENANDO ELEMENTOS DE UNA LISTA SEGUN SU CANTIDAD DE CARACTERES
# Key es una propiedad del metodo sort y se pasa un valor que es el metodo len
ramos.sort(key=len)
print(ramos)

# OCUPANDO EL METODO EXTEND (EXTENDIENDO UNA LISTA A PARTIR DE OTRA)
ramitos = ['Calculo','Automatas'] # Nueva lista creada
ramos.extend(ramitos)
print(ramos)
