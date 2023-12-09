import tkinter as tk

def on_button_click():
    label.config(text="¡Hola, " + entry.get() + "!")

# Crear una ventana
window = tk.Tk()

# Crear y agregar widgets (etiqueta, entrada, botón)
label = tk.Label(window, text="Ingresa tu nombre:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Saludar", command=on_button_click)
button.pack()

# Iniciar el bucle de eventos
window.mainloop()