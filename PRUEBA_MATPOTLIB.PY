import matplotlib.pyplot as plt

# Datos para el gráfico

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el gráfico de líneas
plt.plot(x, y, label='Primos')

# Etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Números Primos')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
