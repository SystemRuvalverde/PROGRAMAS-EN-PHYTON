import tkinter as tk

def abrir_nueva_ventana():
    # Crear una nueva ventana
    nueva_ventana = tk.Toplevel(root)

    # Configurar la nueva ventana
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("300x200")

    # Contenido de la nueva ventana
    etiqueta = tk.Label(nueva_ventana, text="¡Hola! Esta es la nueva ventana.")
    etiqueta.pack(padx=20, pady=20)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("400x300")

# Botón para abrir la nueva ventana
boton = tk.Button(root, text="Abrir Nueva Ventana", command=abrir_nueva_ventana)
boton.pack(pady=20)

# Iniciar el bucle principal
root.mainloop()
