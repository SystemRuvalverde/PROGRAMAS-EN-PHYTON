import random
import names

# Generar 30 datos aleatorios
for _ in range(30):
    nombre = names.get_first_name()
    apellido_paterno = names.get_last_name()
    apellido_materno = names.get_last_name()
    edad = random.randint(18, 80)
    direccion = "Calle " + str(random.randint(1, 100)) + ", Col. " + names.get_last_name()
    sexo = random.choice(["Masculino", "Femenino"])
    curp = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=18))
    rfc = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=13))
    telefono_casa = "55" + ''.join(random.choices('1234567890', k=8))
    telefono_celular = "55" + ''.join(random.choices('1234567890', k=8))
    estado_civil = random.choice(["Soltero/a", "Casado/a", "Viudo/a", "Divorciado/a"])
    ultimo_grado_estudio = random.choice(["Primaria", "Secundaria", "Preparatoria", "Universidad"])
    num_hijos = random.randint(0, 5)
    nombre_hijos = [names.get_full_name() for _ in range(num_hijos)]
    nombre_madre = names.get_full_name()
    nombre_padre = names.get_full_name()
    num_hermanos = random.randint(0, 5)
    nombre_hermanos = [names.get_full_name() for _ in range(num_hermanos)]
    
    # Imprimir los datos generados
    print(f"Nombre: {nombre}")
    print(f"Apellido Paterno: {apellido_paterno}")
    print(f"Apellido Materno: {apellido_materno}")
    print(f"Edad: {edad}")
    print(f"Dirección: {direccion}")
    print(f"Sexo: {sexo}")
    print(f"CURP: {curp}")
    print(f"RFC: {rfc}")
    print(f"Teléfono de Casa: {telefono_casa}")
    print(f"Teléfono Celular: {telefono_celular}")
    print(f"Estado Civil: {estado_civil}")
    print(f"Último Grado de Estudio: {ultimo_grado_estudio}")
    print(f"Número de Hijos: {num_hijos}")
    print(f"Nombre Completo de los Hijos: {', '.join(nombre_hijos)}")
    print(f"Nombre Completo de la Madre: {nombre_madre}")
    print(f"Nombre Completo del Padre: {nombre_padre}")
    print(f"Número de Hermanos: {num_hermanos}")
    print(f"Nombre Completo de los Hermanos: {', '.join(nombre_hermanos)}")
    print("\n")