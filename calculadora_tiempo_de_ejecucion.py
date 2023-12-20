import time

def calcular_tiempo_ejecucion(codigo_a_medir):
    inicio_tiempo = time.time()
    codigo_a_medir()
    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

# Ejemplo de uso:
def codigo_a_medir():
    # Coloca aquí el fragmento de código que deseas medir
    for _ in range(1000000):
        _ = _ + 1

# Llama a la función con el código que deseas medir
calcular_tiempo_ejecucion(codigo_a_medir)