
trasporte = []
#AGREGA 5 VALORES SEPARADOS POR ESPACIO AL ARREGLO
trasporte = input("Ingrese 5 transportes separado por espacios: ").split()


# Haz un bucle 5 veces para llenar la lista con 5 tipos de transporte
for i in range(5):
    print("Ingresa el transporte en el valor", i)
    trasporte.append(str(input()))

print(trasporte)
