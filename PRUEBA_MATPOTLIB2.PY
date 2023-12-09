import matplotlib.pyplot as plt

# Datos para el gráfico
#print("INGRESA 5 VALORES DE W")
w = input("Ingrese 5 valores de W separados por espacios: ").split()

#print("INGRESA 5 VALORES DE X")
x = input("Ingrese 5 valores de X separados por espacios: ").split()

#print("INGRESA 5 VARLORES DE Y") 
y = input("Ingrese 5 valores de Y separados por espacios: ").split()

#print("INGRESA 5 VARLORES DE Z") 
z = input("Ingrese 5 valores de Z separados por espacios: ").split()

        

#x = [13,19,17,23,31]
#y = [2, 3, 5, 7, 11]

# Crear el gráfico de líneas
plt.plot(w,x,label='Multiplos de 2 y 4')
plt.plot(y,z,label='Multiplos de 5 y 10')
# Etiquetas y título
plt.xlabel('Eje W')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.ylabel('Eje Z')
plt.title('Números Primos')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
