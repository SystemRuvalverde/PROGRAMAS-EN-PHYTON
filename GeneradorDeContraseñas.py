import random
import string

def generar_cadena_aleatoria_de_letras(longitud):
    # Utiliza el modulo string para obtener todos los caracteres alfabeticos (mayusculas y minusculas)
    caracteres = string.ascii_letters
    # Genera una cadena aleatoria utilizando random.choices y la cantidad de caracteres especificada
    cadena_aleatoria_de_letras = ''.join(random.choices(caracteres, k=longitud))
    return cadena_aleatoria_de_letras

def generar_numeros_aleatorios(minimo, maximo):
    return random.randint(minimo, maximo)

def generar_cadena_de_simbolos_aleatoria(longitud):
    # Utiliza el modulo string para obtener todos los símbolos
    caracteres = string.punctuation
    # Genera una cadena aleatoria utilizando random.choices y la cantidad de caracteres especificada
    cadena_aleatoria_de_simbolos = ''.join(random.choices(caracteres, k=longitud))
    return cadena_aleatoria_de_simbolos

def mezclar_caracteres(cadena):
    lista_caracteres = list(cadena)
    random.shuffle(lista_caracteres)
    return ''.join(lista_caracteres)

#main
longitud_cadena_letras = 3
minimo = 100
maximo = 1000
longitud_cadena_simbolos = 2

cadena_resultante = (str(generar_cadena_aleatoria_de_letras(longitud_cadena_letras)) + str(generar_numeros_aleatorios(minimo, maximo)) + str(generar_cadena_de_simbolos_aleatoria(longitud_cadena_simbolos)))

cadena_mezclada = mezclar_caracteres(cadena_resultante)

print (cadena_mezclada)