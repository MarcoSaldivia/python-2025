# Datos
productos = ["Smartphone", "Laptop", "Tablet", "Smartwatch"]
precios = [300, 800, 150, 200]

# Stock disponible
stock = {
    "Smartphone": 25,
    "Laptop": 12,
    "Tablet": 8,
    "Smartwatch": 4
}

# Encontrar articulo más caro y mas barato
precio_max = max(precios)
precio_min = min(precios)

indice_max = precios.index(precio_max)
indice_min = precios.index(precio_min)

print(f"Articulo más caro: {productos[indice_max]} - Precio: ${precio_max}")
print(f"Articulo más barato: {productos[indice_min]} - Precio: ${precio_min}")


# Mostrar categoria de precios
for producto, precio in zip(productos, precios):
    if precio < 200:
        categoria = "Producto Economico"
    elif 200 <= precio <= 500:
        categoria = "Producto Estandar"
    else:
        categoria = "Producto Premium"
    print(f"{producto}: {categoria}")


# Lista de articulos con stock bajo
for producto, unidades in stock.items():
    if unidades < 10:
        print(f"{producto} : {unidades}")
