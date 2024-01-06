import tkinter as tk
from tkinter import Toplevel
import mysql.connector
import os
import subprocess
"import CONTROL_DIESEL_ZONA
#import VENTANA_INFORMACION #CON ESTA IMPORTACION SE DEFORMA LA VENTANA_INFORMACION
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
conexion = None

def insertar_datos_cliente(): #FUNCION PARA INSERTAR LOS DATOS
    nombre_chofer_var = entry_nombre.get()
    apellido_chofer_var = entry_apellido.get()
    empresa_chofer_var = entry_empresa.get()
    destino_chofer_var = entry_destino.get()
    
     # Conectar a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user="usuario",
        password="contraseña",
        database="nombre_base_de_datos"
    )
    
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
      
    
  
  

ventana_informacion = False  # Variable para controlar si la ventana de información está abierta
def actualizar_datos(): #FUNCION PARA INSERTAR LOS DATOS
    print("hola")

def eliminar_datos_chofer(): #FUNCION PARA INSERTAR LOS DATOS
    print("hola")

def imprimir_datos(): #FUNCION PARA INSERTAR LOS DATOS
    print("hola")
    
def datos_pdf(): #FUNCION PARA INSERTAR LOS DATOS
    print("hola")


#def mostrar_datos_chofer(): #FUNCION PARA ABRIR SOLO UNA VENTA********************************************************
       #ventana_informacion()