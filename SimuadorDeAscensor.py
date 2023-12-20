import time

class Ascensor:
    def __init__(self, num_pisos):
        self.num_pisos = num_pisos
        self.piso_actual = 1

    def ir_a_piso(self, destino):
        if 1 <= destino <= self.num_pisos:
            print(f"Moviendo el ascensor del piso {self.piso_actual} al piso {destino}.")
            self.piso_actual = destino
        else:
            print(f"El piso {destino} no es válido. Por favor, elija un piso entre 1 y {self.num_pisos}.")

class SimuladorAscensor:
    def __init__(self, num_pisos):
        self.ascensor = Ascensor(num_pisos)

    def ejecutar_simulacion(self):
        while True:
            print(f"Ascensor en el piso {self.ascensor.piso_actual}")
            destino = int(input("Ingrese el piso al que desea ir (o 0 para salir): "))
            
            if destino == 0:
                print("Simulación terminada. ¡Hasta luego!")
                break
            
            self.ascensor.ir_a_piso(destino)
            time.sleep(5)  # Simulación de tiempo de viaje del ascensor

if __name__ == "__main__":
    num_pisos_edificio = 10  # Puedes ajustar la cantidad de pisos según tu necesidad
    simulador = SimuladorAscensor(num_pisos_edificio)
    simulador.ejecutar_simulacion()
