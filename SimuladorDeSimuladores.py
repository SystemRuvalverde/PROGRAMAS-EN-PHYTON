import time

class SimuladorCohetes:
    def __init__(self, nombre):
        self.nombre = nombre

    def lanzar_cohete(self):
        print(f"Lanzando cohete desde el simulador: {self.nombre}")
        time.sleep(2)
        print("¡Cohete lanzado!")

class SimuladorDeSimuladores:
    def __init__(self):
        self.simuladores = []

    def agregar_simulador(self, simulador):
        self.simuladores.append(simulador)

    def ejecutar_simuladores(self):
        print("Ejecutando simuladores...\n")
        for simulador in self.simuladores:
            simulador.lanzar_cohete()
            print("\n---\n")

if __name__ == "__main__":
    simulador1 = SimuladorCohetes("Simulador A")
    simulador2 = SimuladorCohetes("Simulador B")

    simulador_maestro = SimuladorDeSimuladores()
    simulador_maestro.agregar_simulador(simulador1)
    simulador_maestro.agregar_simulador(simulador2)

    simulador_maestro.ejecutar_simuladores()
