import tkinter as tk

#Crear la ventana principal
window = tk.Tk()
window.title("JUEGO DEL GATO")

#Crear y colocar widgets
label = tk.Label(window, text="Bienvenido al juego del gato") #Para dato chofer
label.grid(row=0,column=5,padx=100,pady=10) #ETIQUETA FILA 0 COLUMNA 0
label.config(bg="blue", font="bold")

#*****************************************************************************************************
label = tk.Label(window, text="|                  |")
label.grid(row=2,column=3,padx=100,pady=0)

label = tk.Label(window, text="|                  |")
label.grid(row=3,column=3,padx=100,pady=0)

label = tk.Label(window, text="____________|___________|____________")
label.grid(row=4,column=3,padx=100,pady=0)

label = tk.Label(window, text="|                  |")
label.grid(row=5,column=3,padx=100,pady=0)

label = tk.Label(window, text="|                  |")
label.grid(row=6,column=3,padx=100,pady=0)
               
label = tk.Label(window, text="____________|___________|____________")
label.grid(row=7,column=3,padx=100,pady=0)

label = tk.Label(window, text="|                  |")
label.grid(row=8,column=3,padx=100,pady=0)

label = tk.Label(window, text="|                  |")
label.grid(row=9,column=3,padx=100,pady=0)


#Iniciar el bucle principal de la interfaz
window.mainloop()