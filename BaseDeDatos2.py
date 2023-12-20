import mysql.connector

try:
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        database="tienda"
    )
    
    # Crea un objeto cursor
    cursor = conexion.cursor()

    print("Si deseas insertar datos escribe 1")
    print("Si deseas modificar datos escribe 2")
    print("Si deseas eliminar datos escribe 3")

    opcion = int(input("Elige una opción\n"))
    
    insertar = 0
    actualizar = 0
    eliminar = 0
    
    if opcion == 1:
        print("Has seleccionado la opción: insertar datos")
        # Solicitar entrada de usuario para los datos de la consulta
        nuevo_id_cliente = int(input("Ingresa el id_cliente que quieras insertar\n"))
        nuevo_nombre = input("Ingresa el nombre que quieras insertar\n")
        nueva_direccion = input("Ingresa la dirección que quieras insertar\n")
        nuevo_RFC = input("Ingresa el RFC que quieras insertar\n")
        nuevo_telefono = input("Ingresa el telefono que quieras insertar\n")
        nuevo_id_proveedor = int(input("Ingresa el id_proveedor que quieras insertar\n"))
        # Resto de las variables a eliminar...

       # Query de inserción
        query_insert = "INSERT INTO clientes (ID_CLIENTE, NOMBRE, DIRECCIÓN, RFC, TELEFONO, ID_PROVEEDOR) VALUES (%s, %s, %s, %s, %s, %s)"

        # Ejecuta la consulta de inserción con los valores proporcionados
        cursor.execute(query_insert, (nuevo_id_cliente, nuevo_nombre, nueva_direccion, nuevo_RFC, nuevo_telefono, nuevo_id_proveedor))

        # Antes de confirmar los cambios
        print("Confirmando cambios en la base de datos...")

        # Confirma los cambios en la base de datos
        conexion.commit()

        # Después de confirmar los cambios
        print("Cambios confirmados")

        # Consulta SELECT para obtener los datos actualizados
        query_select = "SELECT * FROM clientes"

        # Antes de ejecutar la consulta SELECT
        print("Ejecutando consulta SELECT...")

        # Ejecuta la consulta SELECT
        cursor.execute(query_select)

        # Recupera todos los resultados
        resultados = cursor.fetchall()

        # Imprime los resultados
        print("\nTabla después de la inserción:")
        for row in resultados:
            print(row)

    elif opcion == 2:
        print("Has seleccionado la opción: modificar datos")
        # Solicitar entrada de usuario para los datos de la consulta
        id_cliente_a_modificar = int(input("Ingresa el ID del cliente que quieres modificar\n"))
        nuevo_nombre = str(input("Ingresa el nuevo nombre\n"))
        nueva_direccion = str(input("Ingresa la nueva dirección\n"))
        nuevo_rfc = str(input("Ingresa el nuevo RFC\n"))
        nuevo_telefono = str(input("Ingresa el nuevo telefono\n"))
        id_proveedor_a_modificar = int(input("Ingresa el ID del proveedor que quieres modificar\n"))

        # Query de modificación
        query_update = "UPDATE clientes SET NOMBRE = %s, DIRECCIÓN = %s, RFC = %s, TELEFONO = %s WHERE ID_CLIENTE = %s AND ID_PROVEEDOR = %s"

        # Antes de ejecutar la consulta de actualización
        print("Ejecutando consulta de actualización...")

        # Ejecuta la consulta de actualización con los valores proporcionados
        cursor.execute(query_update, (nuevo_nombre, nueva_direccion, nuevo_rfc, nuevo_telefono, id_cliente_a_modificar, id_proveedor_a_modificar))

        # Después de ejecutar la consulta de actualización
        print(f"Filas afectadas: {cursor.rowcount}")

        # Antes de confirmar los cambios
        print("Confirmando cambios en la base de datos...")

        # Confirma los cambios en la base de datos
        conexion.commit()

        # Después de confirmar los cambios
        print("Cambios confirmados")

        # Consulta SELECT para obtener los datos actualizados
        query_select = "SELECT * FROM clientes"

        # Antes de ejecutar la consulta SELECT
        print("Ejecutando consulta SELECT...")

        # Ejecuta la consulta SELECT
        cursor.execute(query_select)

        # Recupera todos los resultados
        resultados = cursor.fetchall()

        # Imprime los resultados
        print("\nTabla después de la actualización:")
        for row in resultados:
            print(row)
    
    elif opcion == 3:
        print("Has seleccionado la opción: eliminar datos")
        # Solicitar entrada de usuario para los datos de la consulta
        print("Ingresa el id_cliente que quieras eliminar")
        id_cliente_a_eliminar = int(input())
        print("Ingresa el nombre que quieras eliminar")
        nombre_a_eliminar = input()
        print("Ingresa la dirección que quieras eliminar")
        direccion_a_eliminar = input()
        print("Ingresa el RFC que quieras eliminar")
        RFC_a_eliminar = input()
        print("Ingresa el telefono que quieras eliminar")
        telefono_a_eliminar = input()
        print("Ingresa el id_proveedor que quieras eliminar")
        id_proveedor_a_eliminar = int(input())
        # Resto de las variables a eliminar...

        # Modifica la restricción de clave externa a ON DELETE CASCADE
        alter_query = """ ALTER TABLE proveedor DROP FOREIGN KEY LLAVE_CLIENTE; """
        cursor.execute(alter_query, multi=True)
        conexion.commit()

        # Agrega una pausa para dar tiempo a que la modificación se refleje
        import time
        time.sleep(1)

        alter_query = """
        ALTER TABLE proveedor
        ADD CONSTRAINT LLAVE_CLIENTE
        FOREIGN KEY (ID_PROVEEDOR) REFERENCES clientes(ID_CLIENTE)
        ON DELETE CASCADE;
        """
        cursor.execute(alter_query, multi=True)
        conexion.commit()

        # Query de eliminación
        query_delete = "DELETE FROM clientes WHERE ID_CLIENTE = %s AND NOMBRE = %s AND DIRECCIÓN = %s AND RFC = %s AND TELEFONO = %s AND ID_PROVEEDOR = %s"

        # Antes de ejecutar la consulta de eliminación
        print("Ejecutando consulta de eliminación...")

        # Ejecuta la consulta de eliminación con los valores a eliminar
        cursor.execute(query_delete, (id_cliente_a_eliminar, nombre_a_eliminar, direccion_a_eliminar, RFC_a_eliminar, telefono_a_eliminar, id_proveedor_a_eliminar))

        # Después de ejecutar la consulta de eliminación
        print(f"Filas afectadas: {cursor.rowcount}")

        # Antes de confirmar los cambios
        print("Confirmando cambios en la base de datos...")

        # Confirma los cambios en la base de datos
        conexion.commit()

        # Después de confirmar los cambios
        print("Cambios confirmados")

        # Consulta SELECT para obtener los datos actualizados
        query_select = "SELECT * FROM clientes"

        # Antes de ejecutar la consulta SELECT
        print("Ejecutando consulta SELECT...")

        # Ejecuta la consulta SELECT
        cursor.execute(query_select)

        # Recupera todos los resultados
        resultados = cursor.fetchall()

        # Imprime los resultados
        print("\nTabla después de la eliminación:")
        for row in resultados:
            print(row)
    
    else:
        print ("Opción invalida")
    
except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    # Cierra el cursor y la conexión
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()