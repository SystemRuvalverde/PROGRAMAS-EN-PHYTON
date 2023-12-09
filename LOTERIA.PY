import random

def barajaLoteria():
    
    
# Cartas de lotería para cada jugador
jugador1_cartas = random.sample(range(1, 55), 16)  # Genera 16 cartas aleatorias para el jugador 1
jugador2_cartas = random.sample(range(1, 55), 16)  # Genera 16 cartas aleatorias para el jugador 2

# Función para imprimir las cartas de un jugador
def imprimir_cartas(jugador, cartas):
    print(f"Jugador {jugador} - Cartas:")
    for carta in cartas:
        print(carta)

# Función para verificar si un jugador tiene una carta
def verificar_carta(jugador_cartas, carta):
    return carta in jugador_cartas

# Imprimir las cartas de cada jugador
imprimir_cartas(1, jugador1_cartas)
imprimir_cartas(2, jugador2_cartas)

# Ejemplo de verificación de una carta para el jugador 1
carta_verificar = 
tiene_carta = verificar_carta(jugador1_cartas, carta_verificar)
if tiene_carta:
    print(f"El jugador 1 tiene la carta {carta_verificar}")
else:
    print(f"El jugador 1 no tiene la carta {carta_verificar}")