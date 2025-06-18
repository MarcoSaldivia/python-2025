# A

dic = {
    5700000 : {
        'Ciudad' : 'Castro',
        'Temperatura' : 11.8,
        'Precipitacion' : 2000
    },
    5770000 : {
        'Ciudad' : 'Chonchi',
        'Temperatura' : 8.3,
        'Precipitacion' : 2800
    },
    5790000 : {
        'Ciudad' : 'Quellon',
        'Temperatura' : 10.2,
        'Precipitacion' : 2950
    }
}

print(f"El diccionario es {dic}")



# B
temp_cas = 11.8
temp_cho = 8.3
temp_que = 10.2

try:
    dic[5700000]['Clima'] = temp_cas

    temp_cas = dic[5700000]['Clima']
    if temp_cas > 10:
        dic[5700000]['Clima'] = "Frio"
    elif temp_cas >= 10 and temp_cas <= 15:
        dic[5700000]['Clima'] = "Templado"
    else:
        dic[5700000]['Clima'] = "Calido"


    dic[5770000]['Clima'] = temp_cho

    temp_cho = dic[5770000]['Clima']
    if temp_cho > 10:
        dic[5770000]['Clima'] = "Frio"
    elif temp_cho >= 10 and temp_cho <= 15:
        dic[5770000]['Clima'] = "Templado"
    else:
        dic[5770000]['Clima'] = "Calido"


    dic[5790000]['Clima'] = temp_que

    temp_que = dic[5700000]['Clima']
    if temp_que > 10:
        dic[5790000]['Clima'] = "Frio"
    elif temp_que >= 10 and temp_que <= 15:
        dic[5790000]['Clima'] = "Templado"
    else:
        dic[5790000]['Clima'] = "Calido"
except:
    dic[5700000]['Temp'] = 'Desconocida'
    dic[5770000]['Temp'] = 'Desconocida'
    dic[5790000]['Temp'] = 'Desconocida'


# C
dic[5700000]['Meses mas lluviosos'] = []


dic[5700000]['Meses mas lluviosos'] = ['Mayo']
dic[5770000]['Meses mas lluviosos'] = ['Mayo']
dic[5790000]['Meses mas lluviosos'] = ['Mayo']


dic[5700000]['Meses mas lluviosos'] = ['Mayo', 'Junio']
dic[5770000]['Meses mas lluviosos'] = ['Mayo', 'Junio']
dic[5790000]['Meses mas lluviosos'] = ['Mayo', 'Junio']


dic[5700000]['Meses mas lluviosos'] = ['Mayo', 'Junio', 'Julio']
dic[5770000]['Meses mas lluviosos'] = ['Mayo', 'Junio', 'Julio']
dic[5790000]['Meses mas lluviosos'] =  ['Mayo', 'Junio', 'Julio']



# D

dic[5770000]['Ciudad'] = ['Cudad de los Tres Pisos']




# E
lluvias = [2000, 2800, 2900]

sum_pre = sum(lluvias)
print(f"La suma de las precipitaciones es: {sum_pre}")

max_pre = max(lluvias)
min_pre = min(lluvias)
print(f"Las mayores precipitaciones son: {max_pre}")
print(f"Las menores precipitaciones son: {min_pre}")

print(f"Las maximas precipitaciones son se encuentran en el lugar: {lluvias.index(max_pre)}")


# F
print(dic)



# G

lista = {5700000} = {'Ciudad' : 'Castro'}, {'Temperatura' : 11.8}, {'Precipitacion' : 2000},
        {5770000} = {'Ciudad' : 'Chonchi'}, {'Temperatura' : 8.3},{}'Precipitacion' : 2800},
        {5790000} = {'Ciudad' : 'Quellon'},'Temperatura' : 10.2},{}'Precipitacion' : 2950}.
