i=0
j=0
memoria=0
lista = []
for i in range(0,5):
    print ("Ingresa un número")
    lista.append(int(input()))
    print (" ")
    
for j in range(0,5):
    for i in range(0,5-j-1):
        if lista[i]<lista[i+1]:
            memoria=lista[i+1]
            lista[i+1]=lista[i]
            lista[i]=memoria
            
for i in range(0,5):
    print (lista[i])

