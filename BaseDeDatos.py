import tkinter as tk
from tkinter import messagebox
import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        database="tienda"
    )

def ejecutar_consulta(query, values=None):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()

        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        conexion.commit()
        return cursor.fetchall()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error: {error}")

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def Insertar_cliente(id_cliente, nombre, direccion, rfc, telefono, id_proveedor):
    # Query de inserción
    query_insert = "INSERT INTO clientes (ID_CLIENTE, NOMBRE, DIRECCIÓN, RFC, TELEFONO, ID_PROVEEDOR) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (id_cliente, nombre, direccion, rfc, telefono, id_proveedor)
    ejecutar_consulta(query_insert, values)
            
def Modificar_cliente(id_cliente, nuevo_nombre, nueva_direccion, nuevo_rfc, nuevo_telefono, id_proveedor):
    # Query de actualizacion
    query_update = "UPDATE clientes SET NOMBRE = %s, DIRECCIÓN = %s, RFC = %s, TELEFONO = %s WHERE ID_CLIENTE = %s AND ID_PROVEEDOR"
    values = (id_cliente, nuevo_nombre, nueva_direccion, nuevo_rfc, nuevo_telefono, id_proveedor)
    ejecutar_consulta(query_update, values)
    
def Eliminar_cliente(id_cliente, nombre, direccion, rfc, telefono, id_proveedor):
    # Query de eliminación
    query_delete = "DELETE FROM clientes WHERE ID_CLIENTE = %s AND NOMBRE = %s AND DIRECCIÓN = %s AND RFC = %s AND TELEFONO = %s AND ID_PROVEEDOR = %s"
    values = (id_cliente, nombre, direccion, rfc, telefono, id_proveedor)
    ejecutar_consulta(query_delete, values)

# Crear la ventana principal
def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Tienda")

    # Función para manejar clic en botón
    def on_button_insertar():
        id_cliente = entry_id_cliente.get()
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        rfc = entry_rfc.get()
        telefono = entry_telefono.get()
        id_proveedor = entry_id_proveedor.get()
        Insertar_cliente(id_cliente, nombre, direccion, rfc, telefono, id_proveedor)
        #mostrar_resultados()
        
    def on_button_modificar():
        id_cliente = entry_id_cliente.get()
        nuevo_nombre = entry_nuevo_nombre.get()
        nueva_direccion = entry_nueva_direccion.get()
        nuevo_rfc = entry_nuevo_rfc.get()
        nuevo_telefono = entry_nuevo_telefono.get()
        id_proveedor = entry_id_proveedor.get()
        Modificar_cliente(id_cliente, nuevo_nombre, nueva_direccion, nuevo_rfc, nuevo_telefono, id_proveedor)
        #mostrar_resultados()
        
    def on_button_eliminar():
        id_cliente = entry_id_cliente.get()
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        rfc = entry_rfc.get()
        telefono = entry_telefono.get()
        id_proveedor = entry_id_proveedor.get()
        Eliminar_cliente(id_cliente, nombre, direccion, rfc, telefono, id_proveedor)
        #mostrar_resultados()    
        
    """def mostrar_resultados():
        query_select = "SELECT * FROM clientes"
        resultados = ejecutar_consulta(query_select)
        print ("nTabla actualizada")
        for row in resultados:
            print(row)
        """
    # Widgets
    label_id_cliente = tk.Label(ventana, text="ID_cliente:")
    entry_id_cliente = tk.Entry(ventana)

    label_nombre = tk.Label(ventana, text="Nombre:")
    entry_nombre = tk.Entry(ventana)

    label_direccion = tk.Label(ventana, text="Direccion:")
    entry_direccion = tk.Entry(ventana)

    label_rfc = tk.Label(ventana, text="RFC:")
    entry_rfc = tk.Entry(ventana)

    label_telefono = tk.Label(ventana, text="Telefono:")
    entry_telefono = tk.Entry(ventana)

    label_id_proveedor = tk.Label(ventana, text="ID_proveedor:")
    entry_id_proveedor = tk.Entry(ventana)

    boton_insertar = tk.Button(ventana, text="Insertar_cliente", command=on_button_insertar)
    boton_modificar = tk.Button(ventana, text="Modificar_cliente", command=on_button_modificar)
    boton_eliminar = tk.Button(ventana, text="Eliminar_cliente", command=on_button_eliminar)

    # Posicionamiento de widgets
    label_id_cliente.grid(row=0, column=0, padx=10, pady=10)
    entry_id_cliente.grid(row=0, column=1, padx=10, pady=10)

    label_nombre.grid(row=1, column=0, padx=10, pady=10)
    entry_nombre.grid(row=1, column=1, padx=10, pady=10)

    label_direccion.grid(row=2, column=0, padx=10, pady=10)
    entry_direccion.grid(row=2, column=1, padx=10, pady=10)

    label_rfc.grid(row=3, column=0, padx=10, pady=10)
    entry_rfc.grid(row=3, column=1, padx=10, pady=10)

    label_telefono.grid(row=4, column=0, padx=10, pady=10)
    entry_telefono.grid(row=4, column=1, padx=10, pady=10)

    label_id_proveedor.grid(row=5, column=0, padx=10, pady=10)
    entry_id_proveedor.grid(row=5, column=1, padx=10, pady=10)

    boton_insertar.grid(row=6, column=0, columnspan=2, pady=10)
    boton_modificar.grid(row=7, column=0, columnspan=2, pady=10)
    boton_eliminar.grid(row=8, column=0, columnspan=2, pady=10)

    # Iniciar el bucle de eventos
    ventana.mainloop()

# Llamar a la función para crear la ventana principal
ventana_principal()