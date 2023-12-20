import random

# Definir la clase
class Equipo:
    def __init__(self, nombre_equipo, nombre_grupo):
        self.nombre_equipo = nombre_equipo
        self.puntos = 0
        self.goles = 0
        self.nombre_grupo = nombre_grupo  # Nueva propiedad

class Grupo:
    def __init__(self, nombre_grupo):
        self.nombre_grupo = nombre_grupo
        self.equipos = []

# Función para realizar el sorteo sin repetir equipos
def sorteo_sin_repeticion(equipos):
    equipos_copia = equipos.copy()
    random.shuffle(equipos_copia)
    return equipos_copia

# Definir los nombres de los equipos
nombres_grupos = ["A", "B", "C", "D", "E", "F", "G", "H"]

# Definir los nombres de los equipos
nombres_equipos = ["Atletico de Madrid", "Bayern Múnich", "Benfica", "Borussia Dortmund", "Braga",
                   "BSC Young Boys", "Celtic Glasgow", "Estrella Roja", "FC Arsenal",
                   "FC Barcelona", "FC Copenhage", "FC Oporto", "FC Shakhtar Donetsk",
                   "Feyenoord", "Galatasaray", "Inter de Milan", "Lazio", "Lens",
                   "Manchester City", "Manchester United", "Milan", "Napoli", "Newcastle United",
                   "PSG", "PSV Eindhoven", "RB Leipzing", "RB Salzburgo", "Real Madrid",
                   "Real Sociedad", "Royal Atwerpen FC", "Sevilla", "Union Berlin"]

# Crear los grupos
grupos = [Grupo(nombre_grupo) for nombre_grupo in nombres_grupos]

# Crear los equipos con los nombres
equipos = [Equipo(nombre_equipo, "") for nombre_equipo in nombres_equipos]  # Inicialmente sin grupo

# Asignar equipos a los grupos
for i, equipo in enumerate(sorteo_sin_repeticion(equipos)):
    grupo_actual = grupos[i % len(grupos)]
    equipo.nombre_grupo = grupo_actual.nombre_grupo  # Asignar el nombre del grupo al equipo
    grupo_actual.equipos.append(equipo)

# Función para simular un partido de ida y vuelta y retornar el marcador total
def simular_partido():
    goles_ida_local = random.randint(0, 5)
    goles_ida_visitante = random.randint(0, 5)
    goles_vuelta_local = random.randint(0, 5)
    goles_vuelta_visitante = random.randint(0, 5)
    goles_totales_local = goles_ida_local + goles_vuelta_local
    goles_totales_visitante = goles_ida_visitante + goles_vuelta_visitante
    return goles_totales_local, goles_totales_visitante

# Simular partidos de ida y vuelta y asignar puntos en la fase de grupos
resultados = []
for grupo in grupos:
    print(f"\nResultados del Grupo {grupo.nombre_grupo}:")
    for i in range(len(grupo.equipos)):
        for j in range(i + 1, len(grupo.equipos)):
            # Simular partido de ida
            goles_equipo_i, goles_equipo_j = simular_partido()
            resultados.append((grupo.equipos[i].nombre_equipo, grupo.equipos[j].nombre_equipo, goles_equipo_i, goles_equipo_j))
            grupo.equipos[i].goles += goles_equipo_i
            grupo.equipos[j].goles += goles_equipo_j
            if goles_equipo_i > goles_equipo_j:
                grupo.equipos[i].puntos += 3
            elif goles_equipo_i < goles_equipo_j:
                grupo.equipos[j].puntos += 3
            else:
                grupo.equipos[i].puntos += 1
                grupo.equipos[j].puntos += 1

            # Simular partido de vuelta
            goles_equipo_i, goles_equipo_j = simular_partido()
            resultados.append((grupo.equipos[j].nombre_equipo, grupo.equipos[i].nombre_equipo, goles_equipo_j, goles_equipo_i))
            grupo.equipos[i].goles += goles_equipo_i
            grupo.equipos[j].goles += goles_equipo_j
            if goles_equipo_i > goles_equipo_j:
                grupo.equipos[j].puntos += 3
            elif goles_equipo_i < goles_equipo_j:
                grupo.equipos[i].puntos += 3
            else:
                grupo.equipos[i].puntos += 1
                grupo.equipos[j].puntos += 1

    # Ordenar los equipos dentro del grupo por puntos
    grupo.equipos = sorted(grupo.equipos, key=lambda x: x.puntos, reverse=True)

    # Mostrar resultados de los partidos y tabla del grupo
    for resultado in resultados:
        print(f"{resultado[0]} {resultado[2]} - {resultado[3]} {resultado[1]}")

    print("\nTabla del Grupo", grupo.nombre_grupo + ":")  # Agregar el nombre del grupo
    print("Equipo\t\tPuntos")
    for equipo in grupo.equipos:
        print(f"{equipo.nombre_equipo}\t\t{equipo.puntos}")

    # Reiniciar resultados para el próximo grupo
    resultados = []

# Seleccionar los 16 equipos con más puntos para octavos de final
equipos_octavos = [equipo for grupo in grupos for equipo in grupo.equipos]
equipos_octavos = sorted(equipos_octavos, key=lambda x: x.puntos, reverse=True)[:16]

# Simular octavos de final (partidos de ida y vuelta)
print("\nResultados de los octavos de final:")
equipos_cuartos = []
for i in range(0, 16, 2):
    # Simular partido de ida
    goles_equipo_i, goles_equipo_j = simular_partido()
    print(f"{equipos_octavos[i].nombre_equipo} {goles_equipo_i} - {goles_equipo_j} {equipos_octavos[i+1].nombre_equipo} (Ida)")
    if goles_equipo_i > goles_equipo_j:
        equipos_cuartos.append(equipos_octavos[i])
    else:
        equipos_cuartos.append(equipos_octavos[i + 1])

    # Simular partido de vuelta
    goles_equipo_i, goles_equipo_j = simular_partido()
    print(f"{equipos_octavos[i+1].nombre_equipo} {goles_equipo_j} - {goles_equipo_i} {equipos_octavos[i].nombre_equipo} (Vuelta)")
    if goles_equipo_j > goles_equipo_i:
        equipos_cuartos.append(equipos_octavos[i+1])
    else:
        equipos_cuartos.append(equipos_octavos[i])

# Simular cuartos de final (partidos de ida y vuelta)
print("\nResultados de los cuartos de final:")
equipos_semifinales = []
for i in range(0, 8, 2):
    # Simular partido de ida
    goles_equipo_i, goles_equipo_j = simular_partido()
    print(f"{equipos_cuartos[i].nombre_equipo} {goles_equipo_i} - {goles_equipo_j} {equipos_cuartos[i+1].nombre_equipo} (Ida)")
    if goles_equipo_i > goles_equipo_j:
        equipos_semifinales.append(equipos_cuartos[i])
    else:
        equipos_semifinales.append(equipos_cuartos[i + 1])

    # Simular partido de vuelta
    goles_equipo_i, goles_equipo_j = simular_partido()
    print(f"{equipos_cuartos[i+1].nombre_equipo} {goles_equipo_j} - {goles_equipo_i} {equipos_cuartos[i].nombre_equipo} (Vuelta)")
    if goles_equipo_j > goles_equipo_i:
        equipos_semifinales.append(equipos_cuartos[i+1])
    else:
        equipos_semifinales.append(equipos_cuartos[i])

# Simular semifinales (partidos de ida y vuelta)
print("\nResultados de las semifinales:")
equipos_final = []
for i in range(0, 4, 2):
    # Simular partido de ida
    goles_equipo_i, goles_equipo_j = simular_partido()
    print(f"{equipos_semifinales[i].nombre_equipo} {goles_equipo_i} - {goles_equipo_j} {equipos_semifinales[i + 1].nombre_equipo} (Ida)")
    if goles_equipo_i > goles_equipo_j:
        equipos_final.append(equipos_semifinales[i])
    else:
        equipos_final.append(equipos_semifinales[i + 1])

    # Simular partido de vuelta
    goles_equipo_i, goles_equipo_j = simular_partido()
    print(f"{equipos_semifinales[i + 1].nombre_equipo} {goles_equipo_j} - {goles_equipo_i} {equipos_semifinales[i].nombre_equipo} (Vuelta)")
    if goles_equipo_j > goles_equipo_i:
        equipos_final.append(equipos_semifinales[i + 1])
    else:
        equipos_final.append(equipos_semifinales[i])

# Simular final (partidos de ida y vuelta)
print("\nResultado de la final:")
goles_equipo_i, goles_equipo_j = simular_partido()
print(f"{equipos_final[0].nombre_equipo} {goles_equipo_i} - {goles_equipo_j} {equipos_final[1].nombre_equipo}")

# Determinar el campeón
if goles_equipo_i + goles_equipo_j > goles_equipo_i:
    campeon = equipos_final[1]
else:
    campeon = equipos_final[0]

# Imprimir el campeón del torneo
print("\nEl campeón del torneo es:", campeon.nombre_equipo)
