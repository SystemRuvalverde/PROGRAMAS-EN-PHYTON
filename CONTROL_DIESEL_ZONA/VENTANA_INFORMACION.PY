import tkinter as tk




# Crear la ventana principal
ventana_informacion = tk.Tk()
ventana_informacion.title("VENTANA DE INFORMACION - CONTROL DE DIESEL - ZONA INDUSTRIAL")
label = tk.Label(ventana_informacion,text="FECHA DE SALIDA DE DIESEL") #PARA DATO DE FECHA DE SALIDA DE DIESEL
label.grid(row=7, column=3,padx=10,pady=10) #ETIQUETA FILA 9 COLUMNA 1
label.config(bg="blue",fg="white",font="bold",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry = tk.Entry(ventana_informacion) #PARA ESCRIBIR DATO DE FECHA DE SALIDA DE DIESEL
entry.grid(row=8,column=3,padx=10,pady=10)  # CAJA DE ENTRADA FILA 10 COLUMNA 1
entry.config(bg="blue", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#-------------------------------------ETIQUETAS DE PRUEBA-----------------------------
label = tk.Label(ventana_informacion,text="PRUEBA NOMBRE DE CHOFER") #PARA DATO DE FECHA DE SALIDA DE DIESEL
label.grid(row=7, column=3,padx=10,pady=10) #ETIQUETA FILA 9 COLUMNA 1
label.config(bg="blue",fg="white",font="bold",border=10)# CONFIGURACIÓN COLOR, BORDE

label = tk.Label(ventana_informacion,text="PRUEBA EMPRESA DE CHOFER") #PARA DATO DE FECHA DE SALIDA DE DIESEL
label.grid(row=7, column=3,padx=10,pady=10) #ETIQUETA FILA 9 COLUMNA 1
label.config(bg="blue",fg="white",font="bold",border=10)# CONFIGURACIÓN COLOR, BORDE

label = tk.Label(ventana_informacion,text="PRUEBA MENSAJE: SALUDOS A TODOS") #PARA DATO DE FECHA DE SALIDA DE DIESEL
label.grid(row=7, column=3,padx=10,pady=10) #ETIQUETA FILA 9 COLUMNA 1
label.config(bg="blue",fg="white",font="bold",border=10)# CONFIGURACIÓN COLOR, BORDE