# Diccionario con frutas y sus precios
inventario = {
    "Manzana": (1000, 1100, 1050),
    "Platano": (700, 700, 800),
    "Cereza": (2500, 2400, 2450)
}

# Precios únicos del platano
precios_platano = inventario["Platano"]
precios_unicos = list(set(precios_platano))

# Lista con los nombres de las frutas
tipos_frutas = list(inventario.keys())

# Promedio de los precios únicos del platano
promedio = sum(precios_unicos) / len(precios_unicos)

# Mostrar resultados
print("Inventario:", inventario)
print("Precios únicos del plátano:", precios_unicos)
print("Tipos de frutas:", tipos_frutas)
print("Promedio de precios del plátano:", round(promedio, 3))
