import random

def Sujeto():
    sujetos = ["Gabriela ", "Javier ", "Marta ", "Carlos ", "Ana ", "Rodrigo ", "Valeria ", "Andrés ", "Lucía ", "Diego "]
    return random.choice(sujetos)

def Verbo():
    verbos = ["corre ", "baila ", "salta ", "canta ", "caga ", "escribe ", "nada ", "construye ", "sueña ", "observa ", "explora "]
    return random.choice(verbos)

def Predicado():
    predicados = ["en el bosque", "con entusiasmo", "después de la tormenta", "sin dudar", "durante la noche", "a toda velocidad", "junto al río", "con una sonrisa", "en la cima de la montaña", "bajo la luz de la luna"]
    return random.choice(predicados)

#main
print (Sujeto() + Verbo() + Predicado())