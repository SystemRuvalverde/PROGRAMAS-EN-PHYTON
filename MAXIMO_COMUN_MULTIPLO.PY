import random

def max_resultado(lista,cantidad):
    i = int(0)
    resultado = list[0]
    for i in range(1,cantidad):
        if lista[i] > resultado:
            resultado = lista[i]
    return resultado

def mcm(lista,cantidad):
    MCM = max_resultado(lista,cantidad)
    i = int(0)
    while True:
        for i in range(cantidad):
            if MCM % lista[i] != 0:
                break
        else:
            return MCM
        MCM = 1

lista = [5]
lista.append(random.randint(1,10))
lista.append(random.randint(1,10))
lista.append(random.randint(1,10))
lista.append(random.randint(1,10))
lista.append(random.randint(1,10))

for i in lista:
    print(i)

MCM = mcm(lista,5)
print("El Minimo Comun multiplo es: ", MCM)