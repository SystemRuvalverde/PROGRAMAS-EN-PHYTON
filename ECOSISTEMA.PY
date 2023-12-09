import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros del ecosistema
tamaño_ecosistema = 20
tasa_crecimiento_presas = 0.1
tasa_crecimiento_depredadores = 0.05
tasa_muerte = 0.05
tasa_migracion = 0.02

# Inicialización del ecosistema
presas = np.random.rand(tamaño_ecosistema, tamaño_ecosistema)
depredadores = np.random.rand(tamaño_ecosistema, tamaño_ecosistema)

# Configuración de la figura
fig, ax = plt.subplots()

def actualizar(frame):
    global presas, depredadores

    # Reproducción y muerte de presas
    presas += tasa_crecimiento_presas * presas * (1 - presas) - tasa_muerte * presas - tasa_migracion * (presas - np.roll(presas, 1, axis=0))

    # Reproducción y muerte de depredadores
    depredadores += tasa_crecimiento_depredadores * depredadores * (1 - depredadores) - tasa_muerte * depredadores - tasa_migracion * (depredadores - np.roll(depredadores, 1, axis=0))

    # Asegurar que los valores estén en el rango [0, 1]
    presas = np.clip(presas, 0, 1)
    depredadores = np.clip(depredadores, 0, 1)

    # Visualización del ecosistema
    ax.clear()
    ax.imshow(presas, cmap='Greens', interpolation='nearest', vmin=0, vmax=1)
    ax.imshow(depredadores, cmap='Reds', interpolation='nearest', alpha=0.5, vmin=0, vmax=1)

    ax.set_title(f'Frame {frame}')

# Crear la animación
ani = animation.FuncAnimation(fig, actualizar, frames=100, interval=200)

# Mostrar la animación
plt.show()