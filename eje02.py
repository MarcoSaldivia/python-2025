# Pedir cuántos estudiantes se registraran
while True:
    try:
        cantidad = int(input("¿Cuántos estudiantes desea registrar? "))
        if cantidad > 0:
            break
        else:
            print("Debe ser mayor a 0.")
    except:
        print("Ingrese un numero valido.")

# Pedir el nombre de la asignatura
asignatura = input("Nombre de la asignatura: ")

# Crear listas para guardar los datos
nombres = []
promedios = []

# Registrar estudiantes
for i in range(cantidad):
    print("Estudiante", i + 1)
    nombre = input("Nombre del estudiante: ")
    nombres.append(nombre)

    suma = 0
    for j in range(1, 4):
        while True:
            try:
                nota = float(input("Ingrese nota " + str(j) + ": "))
                if 0.0 <= nota <= 7.0:
                    suma += nota
                    break
                else:
                    print("Debe ser entre 0.0 y 7.0")
            except:
                print("Nota invalida. Intente otra vez.")

    promedio = suma / 3
    promedios.append(promedio)

# Buscar máximo y mínimo
mayor = max(promedios)
menor = min(promedios)
i_max = promedios.index(mayor)
i_min = promedios.index(menor)

print("Resultados de", asignatura)
print("Mejor promedio:", nombres[i_max], "-", round(mayor, 2))
print("Peor promedio:", nombres[i_min], "-", round(menor, 2))

# Mostrar todos los estudiantes
print("Resumen de estudiantes")
for i in range(cantidad):
    print(nombres[i], "Promedio:", round(promedios[i], 2))

    if promedios[i] < 4.0:
        print("Rendimiento: Bajo")
    elif promedios[i] <= 6.0:
        if promedios[i] > 5.0:
            print("Rendimiento: Regular (Becado)")
        else:
            print("Rendimiento: Regular")
    else:
        print("Rendimiento: Alto (Becado)")

# Mostrar reprobados
print("Estudiantes reprobados")
hay_reprobados = False
for i in range(cantidad):
    if promedios[i] < 4.0:
        print("-", nombres[i])
        hay_reprobados = True

if not hay_reprobados:
    print("Ninguno")
