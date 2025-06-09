print


opcion = input("Por favor, elige una opcion (1-3): ")

match opcion:
    case "1":
        print("Has elegido una Hamburguesa. Precio: $5000")
    case "2":
        print("Has elegido Pizza. Precio: $7500")
    case "3":
        print("Has elegido Completo. Precio: $2500")
    case "4":
        print("Opcion no valida. Por favor, elige entre 1 y 3")


# Ejemplo: determinar estacion segun mes
mes = 4 # Abril
match mes:
    case 12 | 1 | 2:
        print("Verano")
    case 3 | 4 | 5:
        print("Otoño")
    case 6 | 7 | 8:
        print("Invierno")
    case 9 | 10 | 11:
        print("Primavera")
    case _:
        print("Mes invalido")

# Ejemplo: saludo segun hora del dia 
hora = 18 # Formato 24hrs
match hora:
    case h if 0 <= h < 6:
        print("Buenas madrugadas")
    case h if 6 <= h < 12:
        print("Buenos dias")
    case h if 12 <= h < 18:
        print("Buenas tardes")
    case h if 18 <= h < 24:
        print("Buenas noches")
    case _:
        print("Hora invalida")


# Patrones compuestos
x = [1, 2, 3]
match x:
    case [a, b, c]: # desagrupando valores de la lista
        print(f"Elementos de la lista x: {a}, {b}, {c}")

datos = {'nombre': 'Marco', 'edad': 18}
match datos:
    case {'nombre': n, 'edad': e}:
        print(f"Nombre: {n}, Edad: {e}")
