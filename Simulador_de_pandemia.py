import numpy as np
import matplotlib.pyplot as plt

#Parametros del modelo SIR
beta = 0.3 # taza de transmision
gama = 0.1 # taza de recuperacion
poblacion = 160 # tamaño de la poblacion
infectados_iniciales = 1 # numero inicial de infectados
dias_simulacion = 1000 #numero de dias a simular

#arreglos para almacenar los resultados del modelo
susceptibles = np.zeros(dias_simulacion)
infectados = np.zeros(dias_simulacion)
recuperados = np.zeros(dias_simulacion)

#inicializacion de la simulacion
susceptibles[0] = poblacion - infectados_iniciales
infectados[0] = infectados_iniciales
recuperados[0] = 0

#simulacion del modelo SIR
for dia in range(1, dias_simulacion):
    nuevas_infecciones = beta * susceptibles[dia - 1] * infectados[dia - 1] / poblacion
    nuevas_recuperaciones = gama * infectados[dia -1]
    
    susceptibles[dia] = susceptibles[dia - 1] - nuevas_infecciones
    infectados[dia] = infectados[dia - 1] + nuevas_infecciones - nuevas_recuperaciones
    recuperados[dia] = recuperados[dia - 1] + nuevas_recuperaciones
    
#visualizacion de los resultados
dias = np.arange(dias_simulacion)
plt.plot(dias, susceptibles, label='Susceptibles')
plt.plot(dias, infectados, label='Infectados')
plt.plot(dias, recuperados, label='Recuperados')
plt.xlabel('Días')
plt.ylabel('Numero de Individuos')
plt.title("Simulación de pandemia covid-19 (Modelo SIR)")
plt.legend()
plt.show()