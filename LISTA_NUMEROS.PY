import random

def Mayor(lista, cantidad):
    resultado = float('-inf')
    for i in range(cantidad):
        if lista[i] > resultado:
            resultado = lista[i]
    return resultado
    
# Main
lista = [0] * 5

for i in range(5):
    lista[i] = random.randint(1, 50)

for i in range(5):
    print(lista[i])

print("El mayor de la lista es: ", Mayor(lista, 5))