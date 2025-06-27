
# A
print("A")

clinica = {
        101 : { 
            'Nombre' : 'Luna',
            'Peso(kg)' : 1.2,
            'Edad(meses)' : 3,
            'Tamaño(cm)' : 30
            },
        102 : { 
            'Nombre' : 'Michi',
            'Peso(kg)' : 0.8,
            'Edad(meses)' : 2,
            'Tamaño(cm)' : 25
            },
        103 : { 
            'Nombre' : 'Pepito',
            'Peso(kg)' : 2.5,
            'Edad(meses)' : 5,
            'Tamaño(cm)' : 35
        }
}


print(clinica)

# B
print("B")

p_101 = 1.2

try:
    if p_101 < 1:
        clinica[101]['Clasificacion-peso'] = 'Bajo peso'
    elif p_101 >= 1 and p_101 <= 4:
        clinica[101]['Clasificacion-peso'] = 'Normal'
    else:
        clinica[101]['Clasificacion-peso'] = 'Sobre peso'
except:
    raise ValueError('No clasificado')


p_102 = 0.8

try:
    if p_102 < 1:
        clinica[102]['Clasificacion-peso'] = 'Bajo peso'
    elif p_102 >= 1 and p_102 <= 4:
        clinica[102]['Clasificacion-peso'] = 'Normal'
    else:
        clinica[102]['Clasificacion-peso'] = 'Sobre peso'
except:
    raise ValueError('No clasificado')


p_103 = 2.5

try:
    if p_103 < 1:
        clinica[103]['Clasificacion-peso'] = 'Bajo peso'
    elif p_103 >= 1 and p_103 <= 4:
        clinica[103]['Clasificacion-peso'] = 'Normal'
    else:
        clinica[103]['Clasificacion-peso'] = 'Sobre peso'
except:
    raise ValueError('No clasificado')

print(clinica)





# C
print("C")

e_101 = 3

try:
    if e_101 < 4:
        clinica[101]['Categoria-etaria'] = 'Cachorro'
    elif e_101 >= 4 and e_101 <= 12:
        clinica[101]['Categoria-etaria'] = 'Joven'
    else:
        clinica[101]['Categoria-etaria'] = 'Adulto'
except:
    raise ValueError('Desconocida')


e_102 = 2

try:
    if e_102 < 4:
        clinica[102]['Categoria-etaria'] = 'Cachorro'
    elif e_102 >= 4 and e_102 <= 12:
        clinica[102]['Categoria-etaria'] = 'Joven'
    else:
        clinica[102]['Categoria-etaria'] = 'Adulto'
except:
    raise ValueError('Desconocida')


e_103 = 5

try:
    if e_103 < 4:
        clinica[103]['Categoria-etaria'] = 'Cachorro'
    elif e_103 >= 4 and e_103 <= 12:
        clinica[103]['Categoria-etaria'] = 'Joven'
    else:
        clinica[103]['Categoria-etaria'] = 'Adulto'
except:
    raise ValueError('Desconocida')



#D
#  ####aaa = list([101 = 1.2], [102 = 0.8], [103 = 2.5])



# E
print("E")

n_ingresogato = str(input("Ingrese el numero de ingreso del gato:  "))
no_gato = input("Ingrese elnombre del gato: ")
peso_gato =  str(input("Ingrese el peso del gato:  "))
edad_gato =  str(input("Ingrese la edad del gato:  "))
t_gato =  str(input("Ingrese el tamaño del gato:  "))

clinica[n_ingresogato]['Nombre'] = no_gato
clinica[n_ingresogato]['Peso(kg)'] = peso_gato
clinica[n_ingresogato]['Edad(meses)'] = edad_gato
clinica[n_ingresogato]['Tmaño(cm)'] = t_gato

print(clinica)






# F
print("F")

n_ingreso = str(input("Ingrese el numero de ingreso del gato:  "))
n_tamaño = str(input("Ingrese el nuevo tamaño del gato:  "))

clinica[n_ingreso]['Tamaño(cm)'] = n_tamaño



# G
print("G")

val_peso = [1.2 , 0.8 , 2.5]

sum = sum(val_peso)
prom = sum / 3

max_peso = max(val_peso)
min_peso = min(val_peso)

num_ingreso = index(min_peso)




