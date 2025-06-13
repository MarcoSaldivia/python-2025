# ingresa  la cantidad de los materiales solicitados
martillo_c = int(input("Por favor ingresar cantidad de martillos: "))
clavos_c = int(input("Por favor ingresar cantidad de clavos: "))
serruchos_c = int(input("Por favor ingresar cantidad de serruchos: "))
tornillos_c = int(input("Por favor ingresar cantidad de tornillos: "))

# Ingresa el precio de cada articulo
martillo = float(input("¿Cual es su precio de los martillos?: "))
clavos = float(input("¿Cual es su precio de los clavos?: "))
serruchos = float(input("¿Cual es su precio de ?: "))
tornillos = float(input("¿Cual es su precio de los tornillo?: "))

# Calcular precio final de los productos
p_martillo = martillo * martillo_c
p_clavos = clavos * clavos_c
p_serruchos = serruchos * serruchos_c
p_tornillos = tornillos * tornillos_c

# Mostrar el precio final 
print(f"El precio final de los martillos es: {round(p_martillo, 2)}")
print(f"El precio final de los martillos es: {round(p_clavos, 2)}")
print(f"El precio final de los martillos es: {round(p_serruchos, 2)}")
print(f"El precio final de los martillos es: {round(p_tornillos, 2)}")

# Precio total
precio_total = p_martillo + p_clavos + p_serruchos + p_tornillos
print(f"El precio total es: {precio_total}")

# El precio maximo
v_max = p_martillo , p_clavos , p_serruchos , p_tornillos
print(f"El precio maximo es: {v_max}")

# El precio minimo
v_min = p_martillo , p_clavos , p_serruchos , p_tornillos
print(f"El precio minimo es: {v_min}")

# Promedio de precios unitarios de los productos
promedio = (martillo + clavos + serruchos + tornillos) /4
print(f"El promedio es de precios unitarios es: {promedio}")

# El valor del iva respecto al precio total
iva = (precio_total * 19) /100
print(f"El iva es: {iva}")
