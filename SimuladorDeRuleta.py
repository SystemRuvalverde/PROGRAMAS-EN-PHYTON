import random

def generar_numero_aleatorio():
    # Genera un número aleatorio entre 0 y 37 (38 posibles resultados en total).
    return random.randint(0, 37)

def jugar_ruleta():
    numero_elegido = int(input("Elige un número entre 0 y 37: "))
    numero_generado = generar_numero_aleatorio()

    print("Número generado en la ruleta:", numero_generado)

    if numero_generado == numero_elegido:
        print("¡Felicidades, has ganado!")
    elif numero_generado == 0:
        print("Empate, el número generado es 0.")
    else:
        print("Lo siento, has perdido.")

# Inicio del juego
while True:
    jugar_ruleta()

    nuevo_intento = input("¿Deseas intentarlo de nuevo? (S para sí, cualquier otra tecla para no): ")
    if nuevo_intento.lower() != 's':
        print("Gracias por tu participación. ¡Vuelve pronto!")
        break