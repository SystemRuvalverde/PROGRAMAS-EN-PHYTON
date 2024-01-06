import tkinter as tk
from tkinter import ttk
from tkinter import Frame
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import simpledialog
import openpyxl
import mysql.connector
import seaborn as sns
import pandas as pd
from reportlab.pdfgen import canvas
import sys
from fpdf import FPDF
import os
import subprocess
#***************************************FUNCIONES - ADICIONALES********************************************
config = { # Conectar a la base de datos 
    "user": "root",
    "password": "",
    "host": "127.0.0.1",
    "database": "diesel"
}
conexion = mysql.connector.connect(**config)
# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()
# Ahora puedes ejecutar consultas SQL y trabajar con la base de datos
cursor.execute("SELECT * FROM chofer")
resultado = cursor.fetchall()
# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

def insertar_datos_chofer(): #FUNCION PARA INSERTAR LOS DATOS EN LA TABLA CHOFER
    nombre_chofer_var =  entry_nombre.get() 
    apellido_chofer_var = entry_apellido.get()
    empresa_chofer_var = entry_empresa.get()
    destino_chofer_var = entry_destino.get()
    # Conectar a la base de datos
    conn = mysql.connector.connect(**config)
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Consulta para insertar los datos en la base de datos
    query_insertar_cliente = "INSERT INTO CHOFER (nombre_chofer,apellido_chofer,empresa,destino) VALUES (%s, %s,%s,%s)" 
    datos_cliente = (nombre_chofer_var, apellido_chofer_var, empresa_chofer_var, destino_chofer_var)
    # Ejecutar la consulta
    cursor.execute(query_insertar_cliente, datos_cliente)
    # Hacer commit para guardar los cambios en la base de datos
    conn.commit()
    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    conn.close()

def insertar_datos_transporte(): #FUNCION PARA INSERTAR LOS DATOS EN LA TABLA TRANSPORTE
    transporte_codigo_var =  entry_codigo.get() 
    transporte_kilometraje_var = entry_kilometraje.get()
    trasnsporte_color_var = entry_color.get()
    # Conectar a la base de datos
    conn = mysql.connector.connect(**config)
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Consulta para insertar los datos en la base de datos
    query_insertar_cliente = "INSERT INTO TRANSPORTE (codigo,kilometraje,color) VALUES (%s, %s,%s)" 
    datos_trasporte = (transporte_codigo_var, transporte_kilometraje_var, trasnsporte_color_var)
    # Ejecutar la consulta
    cursor.execute(query_insertar_cliente, datos_trasporte)
    # Hacer commit para guardar los cambios en la base de datos
    conn.commit()
    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    conn.close() 
 
def insertar_datos_carga_diesel(): #FUNCION PARA INSERTAR LOS DATOS EN LA TABLA CARGA DIESEL
    entrada_diesel_var =  entry_entrada_diesel.get() 
    salida_diesel_var = entry_salida_diesel.get()
    fecha_entrada_diesel_var = entry_entrada_diesel.get()
    fecha_salida_diesel_var = entry_salida_diesel.get()
    litros_tanque_var = entry_litros_tanque.get()
    # Conectar a la base de datos
    conn = mysql.connector.connect(**config)
    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Consulta para insertar los datos en la base de datos *****PENDIENTE REVICION DE LA CONSULTA
    query_insertar_carga_diesel = "INSERT INTO CARGA_DIESEL(LITROS_TANQUE,ENTRADA_LITROS_DIESEL,SALIDA_LITROS_DIESEL,FECHA_ENTRADA_DIESEL,FECHA_SALIDA_DIESEL) VALUES (%s, %s, %s, %s, %s)"
    carga_diesel =(litros_tanque_var,entrada_diesel_var,salida_diesel_var,fecha_entrada_diesel_var,fecha_salida_diesel_var )
    # Ejecutar la consulta
    cursor.execute(query_insertar_carga_diesel, carga_diesel)
    # Hacer commit para guardar los cambios en la base de datos
    conn.commit()
    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    conn.close() 
#****************************************************************************************************************************    
#************************************************FUNCION PARA ACTUALIZAR LOS DATOS*******************************************
#**************************************************************************************************************************** 
def actualizar_datos(): #FUNCION PARA INSERTAR LOS DATOS
    print("hola")

#****************************************************************************************************************************    
#***************************************FUNCION PARA ELIMINAR DATOS DE LA BASE DE DATOS**************************************
#**************************************************************************************************************************** 
def eliminar_datos(nombre,apellido): #FUNCION PARA INSERTAR LOS DATOS
     # Conectar a la base de datos
    conn = mysql.connector.connect(**config)
    # Crea un cursor
    cursor = conn.cursor()

    # Pide al usuario que ingrese el nombre y apellido mediante una ventana emergente
    nombre_chofer = simpledialog.askstring("Eliminar datos", "Ingrese el nombre del chofer:")
    apellido_chofer = simpledialog.askstring("Eliminar datos", "Ingrese el apellido del chofer:")

    # Ejecuta la sentencia DELETE usando los valores ingresados
    sql = "DELETE FROM CHOFER WHERE NOMBRE_CHOFER = %s AND APELLIDO_CHOFER = %s"
    values = (nombre_chofer, apellido_chofer)
    cursor.execute(sql, values)

    # Realiza el commit y cierra la conexión
    conn.commit()
    conn.close()

    # Informa al usuario que los datos han sido eliminados
    mensaje = f"Datos de {nombre_chofer} {apellido_chofer} eliminados correctamente"
    tk.messagebox.showinfo("Eliminación exitosa", mensaje)
  
#****************************************************************************************************************************    
#*******************************************FUNCION PARA IMPRIMIR DIRECTO PARA UN TICKET*************************************
#**************************************************************************************************************************** 
  # Conectar a la base de datos
    conn = mysql.connector.connect(**config)
    # Crea un cursor
    cursor = conn.cursor()

    # Realiza la consulta utilizando los parámetros nombre y apellido
    consulta = "SELECT * FROM CHOFER WHERE NOMBRE_CHOFER = %s AND APELLIDO_CHOFER = %s"
    cursor.execute(consulta, (nombre, apellido))

    # Obtiene los resultados
    resultado = cursor.fetchone()

    # Cierra la conexión
    conn.close()

    return resultado

def obtener_datos_chofer(nombre, apellido):
    # Configura la conexión a la base de datos
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='diesel'
    )

    # Crea un cursor
    cursor = conn.cursor()

    # Realiza la consulta utilizando los parámetros nombre y apellido
    consulta = "SELECT * FROM CHOFER WHERE NOMBRE_CHOFER = %s AND APELLIDO_CHOFER = %s"
    cursor.execute(consulta, (nombre, apellido))

    # Obtiene los resultados
    resultado = cursor.fetchone()

    # Cierra la conexión
    conn.close()

    return resultado


def imprimir_datos(nombre_archivo, nombre, apellido):
     
    # Configura la conexión a la base de datos
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='diesel'
    )

    # Crea un cursor
    cursor = conn.cursor()

    # Realiza la consulta utilizando los parámetros nombre y apellido
    consulta = "SELECT * FROM CHOFER WHERE NOMBRE_CHOFER = %s AND APELLIDO_CHOFER = %s"
    cursor.execute(consulta, (nombre, apellido))

        # Obtiene los resultados
    resultado = cursor.fetchone()
    # Cierra la conexión
    conn.close()
    return resultado


def imprimir_datos(nombre_archivo, nombre, apellido):
     # Obtén la información del chofer desde la base de datos
    informacion_chofer = obtener_datos_chofer(nombre, apellido)

    if informacion_chofer:
        # Tamaño del papel en puntos (1 pulgada = 25.4 mm)
        ancho_papel_mm = 210
        alto_papel_mm = 74
        ancho_papel_pts = ancho_papel_mm * 25.4 / 72  # 1 pulgada = 72 puntos
        alto_papel_pts = alto_papel_mm * 25.4 / 72

        # Crear un archivo PDF
        c = canvas.Canvas(nombre_archivo, pagesize=(ancho_papel_pts, alto_papel_pts))

        # Agregar información al PDF
        y_pos = alto_papel_pts - 20  # Posición inicial en el eje y

        for titulo, valor in zip(cursor.column_names, informacion_chofer):
            texto = f"{titulo}: {valor}"
            c.drawString(10, y_pos, texto)
            y_pos -= 10  # Bajar 10 puntos para la siguiente línea

        # Guardar el PDF
        c.save()

        # Eliminar datos después de generar el ticket
        #eliminar_exitoso = borrar_campos(nombre, apellido)

        """if eliminar_exitoso:
            print(f"Ticket generado correctamente para {nombre} {apellido}")
        else:
            print(f"No se encontraron datos para {nombre} {apellido}")
        """
    
    
#****************************************************************************************************************************    
#************************************************FUNCION PARA SACAR EL REPORTE DE EXCEL**************************************
#**************************************************************************************************************************** 
def datos_pdf():
   print("HOLA MUNDO")
    
    
"""# Establecer la conexión a la base de datos
    conexion = mysql.connector.connect(**config)
    cursor = conexion.cursor()
    # Sentencia SQL
    consulta = 
        SELECT 
        NOMBRE_CHOFER, APELLIDO_CHOFER, EMPRESA, DESTINO, CODIGO,
        KILOMETRAJE, COLOR, ENTRADA_LITROS_DIESEL, FECHA_ENTRADA_DIESEL,
        SALIDA_LITROS_DIESEL, FECHA_SALIDA_DIESEL, LITROS_TANQUE
        FROM 
        CHOFER
        LEFT JOIN TRANSPORTE ON CHOFER.ID_TRANSPORTE = TRANSPORTE.ID_TRANSPORTE
        LEFT JOIN CARGA_DIESEL ON CHOFER.ID_CARGA_DIESEL = CARGA_DIESEL.ID_CARGA_DIESEL
    """
     # Realizar la consulta a la base de datos
"""cursor.execute(consulta)
    resultados = cursor.fetchall()
    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    conexion.close()

    # Crear un objeto PDF
    nombre_archivo = "DATOS_DIESEL.pdf"
    pdf = SimpleDocTemplate(nombre_archivo, pagesize=(letter[1], letter[0]))
    data = []
    # Agregar los encabezados
    encabezados = ["NOMBRE", "APELLIDO", "EMPRESA", "DESTINO", "CODIGO",
                  "KILOMETRAJE", "COLOR", "ENTRADA LTS", "FECHA DE ENTRADA",
                   "SALIDA LTS", "FECHA DE SALIDA", "LTS TANQUE"]
    data.append(encabezados)
    # Agregar los datos a la tabla del PDF
    for fila in resultados:
        data.append(fila)
    # Crear la tabla
    table = Table(data)

    # Ajustar el ancho de las columnas
    ancho_pagina, alto_pagina = letter
    ancho_columnas = [ancho_pagina/12]*12, [alto_pagina/10*10]
    table._argW = ancho_columnas  # Asignar el ancho de las columnas a la tabla

    # Establecer el estilo de la tabla
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (0, 0), 0),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ('VALIGN', (0, 0), (10, 10), 'MIDDLE')])                   
    table.setStyle(style)

    # Calcular y ajustar la altura de las filas
    for i in range(1, len(data)):
            for j in range(len(data[i])):
                alto_celda = table._cell_height(i, j, canv)
                if alto_celda > alto_fila:
                   alto_fila = alto_celda
                   table._argH[i] = alto_fila
    # Agregar la tabla al objeto PDF
    elements = [table]
    pdf.build(elements)
    os.startfile(nombre_archivo)"""
    #****************************************************************************************************************************
    #************************************************FUNCION PARA SACAR EL REPORTE DE EXCEL**************************************
    #****************************************************************************************************************************
def datos_excel():
    # Establecer la conexión a la base de datos
    conexion = mysql.connector.connect(**config)
    # Utilizar pandas para leer la consulta y crear un DataFrame
    cursor = conexion.cursor()
    # Realizar la consulta a la base de datos
    query = """
    SELECT 
        NOMBRE_CHOFER, APELLIDO_CHOFER, EMPRESA, DESTINO, CODIGO,
        KILOMETRAJE, COLOR, ENTRADA_LITROS_DIESEL, FECHA_ENTRADA_DIESEL,
        SALIDA_LITROS_DIESEL, FECHA_SALIDA_DIESEL, LITROS_TANQUE
    FROM 
        CHOFER
        LEFT JOIN TRANSPORTE ON CHOFER.ID_TRANSPORTE = TRANSPORTE.ID_TRANSPORTE
        LEFT JOIN CARGA_DIESEL ON CHOFER.ID_CARGA_DIESEL = CARGA_DIESEL.ID_CARGA_DIESEL
    """
    # Utilizar pandas para leer la consulta y crear un DataFrame
    df = pd.read_sql(query, conexion)
    # Guardar los resultados en un archivo de Excel
    nombre_archivo = "DATOS_DIESEL.xlsx"
    df.to_excel(nombre_archivo, index=False)
    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    conexion.close()
    # Abrir el archivo de Excel
    os.system("start EXCEL.EXE %s" % nombre_archivo)
    # Abrir el archivo de Excel
    os.startfile(nombre_archivo)
#****************************************************************************************************************************    
#*****************************************FUNCION PARA BORRAR LOS CAMPOS DE LA INTERFAZ**************************************
#**************************************************************************************************************************** 
def borrar_campos(): #FUNCION PARA INSERTAR LOS DATOS
    entry_nombre.delete(0, "end")  # Borra desde el índice 0 hasta el final del texto
    entry_apellido.delete(0, "end")
    entry_empresa.delete(0, "end")
    entry_destino.delete(0, "end")
    entry_codigo.delete(0, "end")
    entry_kilometraje.delete(0, "end")
    entry_color.delete(0, "end")
    entry_entrada_diesel.delete(0, "end")
    entry_salida_diesel.delete(0, "end")
    entry_fecha_entrada_diesel.delete(0, "end")
    entry_fecha_salida_diesel.delete(0, "end")
    entry_litros_tanque.delete(0,"end")
            
#****************************************************************************************************************************    
#************************************************FUNCION PARA FUENTE DE CABEZADOS********************************************
#**************************************************************************************************************************** 
def fuente_encabezados(tabla,tamaño, negrita):
    estilo = ttk.Style()
    estilo.configure('EstiloEncabezado.Treeview.Heading', font=('Helvetica', tamaño, 'bold' if negrita else 'normal'))     
#****************************************************************************************************************************    
#**************************************FUNCION PARA MOSTRAR UNA NUEVA VENTANA CON INFORMACION********************************
#**************************************************************************************************************************** 
def mostrar_datos_ventana_informacion():
    ventana_datos = tk.Toplevel()
    # Conectar a la base de datos (reemplazar con tus propias credenciales y detalles de conexión)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Realizar la consulta
    consulta = """
        SELECT 
        NOMBRE_CHOFER, APELLIDO_CHOFER, EMPRESA, DESTINO, CODIGO,
        KILOMETRAJE, COLOR, ENTRADA_LITROS_DIESEL, FECHA_ENTRADA_DIESEL,
        SALIDA_LITROS_DIESEL, FECHA_SALIDA_DIESEL, LITROS_TANQUE
        FROM 
        CHOFER
        LEFT JOIN TRANSPORTE ON CHOFER.ID_TRANSPORTE = TRANSPORTE.ID_TRANSPORTE
        LEFT JOIN CARGA_DIESEL ON CHOFER.ID_CARGA_DIESEL = CARGA_DIESEL.ID_CARGA_DIESEL
    """

    cursor.execute(consulta)
    resultados = cursor.fetchall()

    # Crear una tabla para mostrar los resultados
    tabla = ttk.Treeview(ventana_datos, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), show="headings")
    tabla.grid(row=0, column=0)

    # Configurar los encabezados de las columnas
    encabezados = ["Nombre Chofer", "Apellido Chofer", "Empresa", "Destino", "Código",
                   "Kilometraje", "Color", "Entrada de Litros", "Fecha de Entrada",
                   "Salida de Litros", "Fecha de Salida", "Litros en Tanque"]

    for i, encabezado in enumerate(encabezados):
        tabla.heading(i+1, text=encabezado)
        tabla.column(i+1, width=120)  # Ancho de la columna

       # Agregar los datos a la tabla con colores alternados
    for i, fila in enumerate(resultados):
        if i % 2 == 0:
            tabla.insert("", "end", values=fila, tags=("even",))
        else:
            tabla.insert("", "end", values=fila, tags=("odd",))

    # Definir los estilos de color para filas pares e impares
    tabla.tag_configure("even", background="lightgray")
    tabla.tag_configure("odd", background="white")
    
    # Agregar los datos a la tabla
    #for fila in resultados:
    #   tabla.insert("", "end", values=fila)

    # Cerrar la conexión a la base de datos
    conn.close()

# Crear la ventana principal
window = tk.Tk()
window.title("CONTROL DE DIESEL - ZONA INDUSTRIAL")

# Crear y colocar widgets
label = tk.Label(window, text="CHOFER") #PARA DATO CHOFER
label.grid(row=0,column=2,padx=10,pady=10) #ETIQUETA FILA 0 COLUMNA 2
label.config(bg="yellow", font="bold", border=10,highlightcolor="black", highlightbackground="black", highlightthickness=5)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#label.config(font="bold", highlightcolor="orange", highlightbackground="orange", highlightthickness=5)

#***********************************************************************************
label_nombre = tk.Label(text="NOMBRE") #PARA DATO NOMBRE
label_nombre.grid(row=1, column=0,padx=10,pady=10) #ETIQUETA FILA 1 COLUMNA 0
label_nombre.config(bg="yellow", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_nombre = tk.Entry(window) #PARA ESCRIBIR DATO NOMBRE
entry_nombre.grid(row=1, column=1,padx=10,pady=10) # CAJA DE ENTRADA FILA 1 COLUMNA 0
entry_nombre.config(bg="yellow", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

#***********************************************************************************
label_apellido = tk.Label(window, text="APELLIDO") #PARA DATO APELLIDO
label_apellido.grid(row=1, column=2,padx=10,pady=10) #ETIQUETA FILA 1 COLUMNA 2
label_apellido.config(bg="yellow", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_apellido = tk.Entry(window) #PARA ESCRIBIR DATO APELLIDO
entry_apellido.grid(row=1, column=3,padx=10,pady=10)  # CAJA DE ENTRADA FILA 1 COLUMNA 3
entry_apellido.config(bg="yellow", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_empresa = tk.Label(window, text="EMPRESA") #PARA DATO EMPRESA
label_empresa.grid(row=2, column=0,padx=10,pady=10) #ETIQUETA FILA 2 COLUMNA 0
label_empresa.config(bg="yellow", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_empresa = tk.Entry(window) #PARA ESCRIBIR DATO EMPRESA
entry_empresa.grid(row=2, column=1,padx=10,pady=10)  # CAJA DE ENTRADA FILA 2 COLUMNA 1
entry_empresa.config(bg="yellow", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_destino = tk.Label(window, text="DESTINO") #PARA DATO DESTINO
label_destino.grid(row=2, column=2,padx=10,pady=10) #ETIQUETA FILA 2 COLUMNA 2
label_destino.config(bg="yellow", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_destino = tk.Entry(window) #PARA ESCRIBIR DATO DESTINO
entry_destino.grid(row=2, column=3,padx=10,pady=10)  # CAJA DE ENTRADA FILA 2 COLUMNA 3
entry_destino.config(bg="yellow", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_transporte = tk.Label(window, text="TRASPORTE:") #PARA DATO TRASPORTE 
label_transporte.grid(row=3, column=2,padx=10,pady=10) #ETIQUETA FILA 3 COLUMNA 2
label_transporte.config(bg="#00FF0F", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_codigo = tk.Label(window, text="CODIGO") #PARA DATO CODIGO
label_codigo.grid(row=4, column=0,padx=10,pady=10) #ETIQUETA FILA 2 COLUMNA 2
label_codigo.config(bg="#00FF0F", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_codigo = tk.Entry(window) #PARA ESCRIBIR DATO CODIGO
entry_codigo.grid(row=5, column=0,padx=10,pady=10)  # CAJA DE ENTRADA FILA 5 COLUMNA 0
entry_codigo.config(bg="#00FF0F", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_kilometraje = tk.Label(window, text="KILOMETRAJE") #PARA DATO KILOMETRAJE
label_kilometraje.grid(row=4, column=1,padx=10,pady=10) #ETIQUETA FILA 2 COLUMNA 2
label_kilometraje.config(bg="#00FF0F", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_kilometraje = tk.Entry(window) #PARA ESCRIBIR DATO KILOMETRAJE
entry_kilometraje.grid(row=5, column=1,padx=10,pady=10)  # CAJA DE ENTRADA FILA 5 COLUMNA 1
entry_kilometraje.config(bg="#00FF0F", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_color = tk.Label(window, text="COLOR") #PARA DATO COLOR
label_color.grid(row=4, column=2,padx=10,pady=10) #ETIQUETA FILA 4 COLUMNA 2
label_color.config(bg="#00FF0F", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_color = tk.Entry(window) #PARA ESCRIBIR DATO COLOR
entry_color.grid(row=5, column=2,padx=10,pady=10)  # CAJA DE ENTRADA FILA 5 COLUMNA 2
entry_color.config(bg="#00FF0F", font="bold", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_carga_diesel = tk.Label(window, text="CARGA DIESEL") #PARA DATO CARGA DIESEL
label_carga_diesel.grid(row=6, column=2,padx=10,pady=10) #ETIQUETA FILA 6 COLUMNA 2
label_carga_diesel.config(bg="blue",fg="white",font="bold",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_entrada_diesel = tk.Label(window, text="ENTRADA DE DIESEL") #PARA DATO ENTRADA DE DIESEL
label_entrada_diesel.grid(row=7, column=0,padx=10,pady=10) #ETIQUETA FILA 7 COLUMNA 0
label_entrada_diesel.config(bg="blue",fg="white",font="bold",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_entrada_diesel = tk.Entry(window) #PARA ESCRIBIR DATO ENTRADA DE DIESEL
entry_entrada_diesel.grid(row=8, column=0,padx=10,pady=10)  # CAJA DE ENTRADA FILA 8 COLUMNA 0
entry_entrada_diesel.config(bg="blue", font="bold",fg="white", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_fecha_entrada_diesel = tk.Label(window, text="FECHA DE ENTRADA DE DIESEL") #PARA DATO FECHA DE ENTRADA DE DIESEL
label_fecha_entrada_diesel.grid(row=7, column=1,padx=10,pady=10) #ETIQUETA FILA 7 COLUMNA 1
label_fecha_entrada_diesel.config(bg="blue",fg="white",font="bold",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_fecha_entrada_diesel = tk.Entry(window) #PARA ESCRIBIR DATO FECHA DE ENTRADA DE DIESEL
entry_fecha_entrada_diesel.grid(row=8, column=1,padx=10,pady=10)  # CAJA DE ENTRADA FILA 8 COLUMNA 1
entry_fecha_entrada_diesel.config(bg="blue", font="bold",fg="white", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_litros_tanque = tk.Label(window, text="LITROS DE TANQUE") #PARA DATO LITROS DE TANQUE
label_litros_tanque.grid(row=9, column=1,padx=10,pady=10) #ETIQUETA FILA 8 COLUMNA 3
label_litros_tanque.config(bg="blue",fg="white",font="bold",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_litros_tanque = tk.Entry(window) #PARA ESCRIBIR DATO LITROS DE TANQUE
entry_litros_tanque.grid(row=9, column=2,padx=10,pady=10)  # CAJA DE ENTRADA FILA 9 COLUMNA 3
entry_litros_tanque.config(bg="blue",font="bold",fg="white", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_salida_diesel = tk.Label(window, text="SALIDA DE DIESEL") #PARA DATO DE SALIDA DE DIESEL
label_salida_diesel.grid(row=7, column=2,padx=10,pady=10) #ETIQUETA FILA 9 COLUMNA 0
label_salida_diesel.config(bg="blue",fg="white",font="bold",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_salida_diesel = tk.Entry(window) #PARA ESCRIBIR DATO DE SALIDA DE DIESEL
entry_salida_diesel.grid(row=8, column=2,padx=10,pady=10)  # CAJA DE ENTRADA FILA 10 COLUMNA 0
entry_salida_diesel.config(bg="blue", font="bold",fg="white", border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#***********************************************************************************
label_fecha_salida_diesel = tk.Label(window, text="FECHA DE SALIDA DE DIESEL") #PARA DATO DE FECHA DE SALIDA DE DIESEL
label_fecha_salida_diesel.grid(row=7, column=3,padx=10,pady=10) #ETIQUETA FILA 9 COLUMNA 1
label_fecha_salida_diesel.config(bg="blue",fg="white",font="bold",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO

entry_fecha_salida_diesel = tk.Entry(window) #PARA ESCRIBIR DATO DE FECHA DE SALIDA DE DIESEL
entry_fecha_salida_diesel.grid(row=8, column=3,padx=10,pady=10)  # CAJA DE ENTRADA FILA 10 COLUMNA 1
entry_fecha_salida_diesel.config(bg="blue", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO
#********************************FUNCIONES - BOTONES**********************************************
boton_agregar_carga_diesel = tk.Button(text="AGREGAR CARGA DIESEL" ,command=insertar_datos_carga_diesel) #CAMBIAR COMMAND         
boton_agregar_carga_diesel.grid(row=2, column=4, padx=10, pady=10)
boton_agregar_carga_diesel.config(bg="red", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO#

boton_agregar_trasporte = tk.Button(text="AGREGAR TRANSPORTE" ,command=insertar_datos_transporte) #CAMBIAR COMMAND         
boton_agregar_trasporte.grid(row=1, column=4, padx=10, pady=10)
boton_agregar_trasporte.config(bg="red", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO#

boton_agregar_datos = tk.Button(text="AGREGAR CHOFER" ,command=insertar_datos_chofer) #CAMBIAR COMMAND         
boton_agregar_datos.grid(row=0, column=4, padx=10, pady=10)
boton_agregar_datos.config(bg="red", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO#

boton_eliminar_datos = tk.Button(text="ELIMINAR DATOS" ,command=eliminar_datos) #CAMBIAR COMMAND         
boton_eliminar_datos.grid(row=9, column=4, padx=10, pady=10)
boton_eliminar_datos.config(bg="red", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO#

boton_mostrar_datos = tk.Button(text="MOSTRAR DATOS" ,command=mostrar_datos_ventana_informacion) #CAMBIAR COMMAND         
boton_mostrar_datos.grid(row=4, column=4, padx=10, pady=10)
boton_mostrar_datos.config(bg="red", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO#

boton_imprimir_datos = tk.Button(text="IMPRIMIR" ,command= imprimir_datos)          
boton_imprimir_datos.grid(row=5, column=4, padx=10, pady=10)
boton_imprimir_datos.config(bg="red", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO#

boton_datos_pdf = tk.Button(text="ABRIR PDF" ,command=datos_pdf)#CAMBIAR COMMAND           
boton_datos_pdf.grid(row=6, column=4, padx=10, pady=10)
boton_datos_pdf.config(bg="red", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO#

boton_datos_pdf = tk.Button(text="ABRIR EXCEL" ,command=datos_excel)#CAMBIAR COMMAND           
boton_datos_pdf.grid(row=7, column=4, padx=10, pady=10)
boton_datos_pdf.config(bg="red", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO#

boton_borrar_datos = tk.Button(text="BORRAR CAMPOS", command=lambda: borrar_campos()) #CAMBIAR COMMAND         
boton_borrar_datos.grid(row=3, column=4, padx=10, pady=10)
boton_borrar_datos.config(bg="red", font="bold",fg="white",border=10)# CONFIGURACIÓN COLOR, BORDE, ANCHO#


#button = tk.Button(window, text="Saludar", command=borrar_datos)
#button.pack("-fill")
#button.config(fg="#03D9FF")


# Iniciar el bucle principal de la interfaz
window.mainloop()