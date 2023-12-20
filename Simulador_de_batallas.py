class Ejercito:
    def __init__(self, nombre, soldados):
        self.nombre = nombre
        self.soldados = soldados

    def atacar(self):
        return sum([soldado.atacar() for soldado in self.soldados])

    def recibir_ataque(self, poder_ataque):
        bajas = min(poder_ataque // len(self.soldados), len(self.soldados))
        self.soldados = self.soldados[bajas:]
        return bajas

class Soldado:
    def __init__(self, nombre, fuerza, resistencia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.resistencia = resistencia

    def atacar(self):
        return self.fuerza

# Función para simular una batalla entre dos ejércitos
def simular_batalla(ejercito1, ejercito2):
    while ejercito1.soldados and ejercito2.soldados:
        poder_ataque_ejercito1 = ejercito1.atacar()
        bajas_ejercito2 = ejercito2.recibir_ataque(poder_ataque_ejercito1)
        print(f"{ejercito1.nombre} ataca a {ejercito2.nombre} con un poder de {poder_ataque_ejercito1}. {ejercito2.nombre} sufre {bajas_ejercito2} bajas.")
        if ejercito2.soldados:
            poder_ataque_ejercito2 = ejercito2.atacar()
            bajas_ejercito1 = ejercito1.recibir_ataque(poder_ataque_ejercito2)
            print(f"{ejercito2.nombre} contraataca a {ejercito1.nombre} con un poder de {poder_ataque_ejercito2}. {ejercito1.nombre} sufre {bajas_ejercito1} bajas.")

    if ejercito1.soldados:
        print(f"{ejercito1.nombre} ha ganado la batalla.")
    else:
        print(f"{ejercito2.nombre} ha ganado la batalla.")

# Crear ejércitos y soldados
ejercito_romano = Ejercito("Ejército Romano", [Soldado("Legionario", 10, 5) for _ in range(100)])
ejercito_cartagines = Ejercito("Ejército Cartaginense", [Soldado("Guerrero Cartaginense", 8, 6) for _ in range(100)])

# Simular la batalla
simular_batalla(ejercito_romano, ejercito_cartagines)
