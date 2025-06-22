edad = 19

if edad > 18:
    print('Eres mayor de edad')
print('Este print esta duera del if') # ESTO ESTA MAL, fijarse el usar del shift


# If = si , else = sino , elif = una tercera opcion
# elif siempre va entre el if y else
# and = para comprobar que se cumplen las dos cosas
if edad > 18 and edad < 65:
    print('Eres mayor de edad')
elif edad > 65:
    print('Eres un adulto mayor')
else:
    print('Eres menor de edad')


# Otra forma de hacerlo, NO RECOMENDADA
edad = 19
print("Usted puede votar" if edad > 18 else "Usted no puede votar")


# Fore = Invoca los colores
# init = inicia la biblioteca
from colorama import init, Fore
init()
print(Fore.MAGENTA + '######## 01 - UTILIZANDO IF Y ELSE ########')

licencia = False
edad = 19
automovil = False

# Utilizando if, elif y else
if licencia and edad >= 18:
    print('Puedo conducir porque soy mayor de edad y tengo licencia')
elif automovil:
    print('Tengo automovil, pero no tengolicencia ni la edad necesaria')
else:
    print('No puedo conducir no tengo ni la edad, ni la licencia ni automovil')
