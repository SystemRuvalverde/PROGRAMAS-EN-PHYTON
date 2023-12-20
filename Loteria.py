import random

cartas = ["El gallo", "El diablito", "La dama", "El catrín", "El paraguas", "La sirena", 
          "La escalera", "La botella", "El barril", "El árbol", "El melón", "El valiente", 
          "El gorrito", "La muerte", "La pera", "La bandera", "El bandolón", "El violoncello",
          "La garza", "El pájaro", "La mano", "La bota", "La luna", "El cotorro", "El borracho",
          "El negrito", "El corazón", "La sandía", "El tambor", "El camarón", "Las jaras",
          "El músico", "La araña", "El soldado", "La estrella", "El cazo", "El mundo", "El apache",
          "El nopal", "El alacrán", "La rosa", "La calavera", "La campana", "El cantarito", 
          "El venado", "El sol", "La corona", "La chalupa", "El pino", "El pescado", "La palma",
          "La maceta", "El arpa", "La rana",]

random.shuffle(cartas)

def Carta_jugador(cartas, cantidad):
    return cartas[:cantidad]

def Carta_lanzada(cartas_lanzadas, cartas_disponibles):
    if not cartas_disponibles:
        return None  # No hay más cartas disponibles
    carta_lanzada = random.choice(cartas_disponibles)
    cartas_disponibles.remove(carta_lanzada)
    cartas_lanzadas.append(carta_lanzada)
    return carta_lanzada

def Imprimir_cartas(CartaJugador):
    for i in range(0, len(CartaJugador), 4):
        fila = CartaJugador[i:i+4]
        print(fila)

def verificar_victoria(cartas_jugador, cartas_lanzadas):
    contador_jugador = {carta: cartas_jugador.count(carta) for carta in set(cartas_jugador)}
    contador_lanzadas = {carta: cartas_lanzadas.count(carta) for carta in set(cartas_lanzadas)}
    
    return all(contador_jugador.get(carta, 0) <= contador_lanzadas.get(carta, 0) for carta in set(cartas_jugador))

def Turno_jugador(jugador):
    print("Turno de", jugador)
    cartas_jugador = Carta_jugador(cartas, 16)
    Imprimir_cartas(cartas_jugador)
    return cartas_jugador

print("Esta es la carta del jugador 1")
CartaJugador1 = Turno_jugador("Jugador 1")
print(" ")
print("Esta es la carta del jugador 2")
CartaJugador2 = Turno_jugador("Jugador 2")
print(" ")

print("Se va y se corre con:")
cartas_lanzadas = []

while True:
    carta_lanzada = Carta_lanzada(cartas_lanzadas, cartas)

    print(carta_lanzada)

    if verificar_victoria(CartaJugador1, cartas_lanzadas):
        print("¡Ha ganado el jugador 1!")
        break
    
    if verificar_victoria(CartaJugador2, cartas_lanzadas):
        print("¡Ha ganado el jugador 2!")
        break

    continuar = input("Presiona Enter para lanzar carta o 's' para salir: ")
    if continuar.lower() == 's':
        break
