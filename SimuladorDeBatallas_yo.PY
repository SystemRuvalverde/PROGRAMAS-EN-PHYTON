class Jugadores:
    def __init__(self, nombre, jugadores):
        self.nombre = nombre
        self.jugadores = jugadores
        
    def atacar(self):
        return sum([jugador.atacar() for jugador in self.jugadores])

    def recibir_ataque(self, poder_ataque):
        corazones_perdidos = min(poder_ataque // len(self.jugadores), len(self.jugadores))
        self.jugadores = self.jugadores[corazones_perdidos:]
        return corazones_perdidos
    
class Jugador:
    def __init__(self, nombre, resistencia):
        self.nombre = nombre
        self.resistencia = resistencia
        
    def atacar(self):
        return 1

class Mobs:
    def __init__(self, nombre, zombies):
        self.nombre = nombre
        self.zombies = zombies
        
    def atacar(self):
        return sum([zombie.atacar() for zombie in self.zombies])

    def recibir_ataque(self, poder_ataque):
        corazones_perdidos = min(poder_ataque // len(self.zombies), len(self.zombies))
        self.zombies = self.zombies[corazones_perdidos:]
        return corazones_perdidos
    
class Zombie:
    def __init__(self, resistencia):
        self.resistencia = resistencia
        
    def atacar(self):
        return 1
    
# Función para simular una batalla entre dos ejércitos
def simular_batalla(jugador, zombie):
    while jugador.jugadores and zombie.zombies:
        poder_ataque_jugador = jugador.atacar()
        corazones_perdidos_zombie = zombie.recibir_ataque(poder_ataque_jugador)
        print(f"{jugador.nombre} ataca a {zombie.nombre} con un poder de {poder_ataque_jugador}. {zombie.nombre} sufre {corazones_perdidos_zombie} corazones perdidos.")
       
        if zombie.zombies:
            poder_ataque_zombie = zombie.atacar()
            corazones_perdidos_jugador = jugador.recibir_ataque(poder_ataque_zombie)
            print(f"{zombie.nombre} contraataca a {jugador.nombre} con un poder de {poder_ataque_zombie}. {jugador.nombre} sufre {corazones_perdidos_jugador} corazones perdidos.")

    if jugador.jugadores:
        print(f"{jugador.nombre} ha ganado la batalla.")
    else:
        print(f"{zombie.nombre} ha ganado la batalla.")

# Crear zombies y jugadores
jugador = Jugadores("Jugador", [Jugador("Jugador", 1) for _ in range(100)])
zombie = Mobs("Zombie", [Zombie(1) for _ in range(100)])

# Simular la batalla
simular_batalla(jugador, zombie)