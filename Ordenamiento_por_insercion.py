def mostrarLista(lista):
    for elemento in lista:
        print(elemento, end=' ')
    print()
numeros = (input("Escribe 5 numeros sin repetir y con espacios: "))
lista = [int(numero) for numero in numeros.split()]
ultimo = len(lista)

for i in range(1, ultimo):
    clave = lista[i]
    j = i-1

    while j >= 0 and lista[j] > clave:
        lista[j+1] = lista[j]
        j = j-1

    lista[j+1] = clave
    mostrarLista(lista)

mostrarLista(lista)