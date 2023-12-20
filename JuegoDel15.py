import tkinter as tk
import random

def mover_boton(fila, columna):
    # Obtener la posición del espacio vacío
    fila_vacia, columna_vacia = obtener_posicion_vacia()

    # Verificar si el movimiento es válido
    if (fila == fila_vacia and abs(columna - columna_vacia) == 1) or \
       (columna == columna_vacia and abs(fila - fila_vacia) == 1):
        # Intercambiar los textos de los botones
        botones[fila - 2][columna - 2]["text"], botones[fila_vacia - 2][columna_vacia - 2]["text"] = \
            botones[fila_vacia - 2][columna_vacia - 2]["text"], botones[fila - 2][columna - 2]["text"]
        actualizar_botones()
        verificar_ganador()

def obtener_posicion_vacia():
    # Encontrar la posición del espacio vacío
    for i in range(4):
        for j in range(4):
            if botones[i][j]["text"] == "":
                return i + 2, j + 2

def actualizar_botones():
    # Actualizar el estado visual de los botones
    for i in range(4):
        for j in range(4):
            texto_boton = botones[i][j]["text"]
            botones[i][j].config(bg="blue", font="bold", fg="white", border=10)
            if texto_boton == "":
                botones[i][j].config(bg="white")  # Color diferente para el espacio vacío
                
def verificar_ganador():
    numeros_ordenados = list(range(1, 16)) + [""]# + [16]
    numeros_actuales = [boton["text"] for fila in botones for boton in fila]
    if numeros_actuales == numeros_ordenados:
        tk.messagebox.showinfo("¡Ganaste!", "Felicidades, has completado el juego del 15.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego del 15")

# Crear una lista con los números del 1 al 15 y espacio vacío
numeros = list(range(1, 16))
numeros.append("")

# Barajar los números de forma aleatoria
random.shuffle(numeros)

# Crear los botones en una matriz
botones = []
for i in range(4):
    fila_botones = []
    for j in range(4):
        texto_boton = numeros.pop(0)
        boton = tk.Button(ventana, text=str(texto_boton), width=3, command=lambda fila=i + 2, col=j + 2: mover_boton(fila, col))
        boton.grid(row=i + 2, column=j + 2, padx=0, pady=0)
        fila_botones.append(boton)
    botones.append(fila_botones)

# Ajustar el espaciado de las columnas y filas
for i in range(2, 6):
    ventana.grid_rowconfigure(i, minsize=0)
    ventana.grid_columnconfigure(i, minsize=0)  

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
