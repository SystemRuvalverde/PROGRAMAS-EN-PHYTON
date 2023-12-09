def numeros_primos(numero):
    divisores=0
    i=0
    for  i in range(1,numero):
        if (numero % i == 0):
            divisores=divisores+1
    if divisores == 1:
        print("El numero",numero,"es un numero primo")
    else: 
        print ("el numero", numero, "no es numero primo")
    return numero
#MAIN
i = int(0)
ultimo = int(0)
print ("Hasta que numero quieres Analizar")
ultimo = int(input())
for i in range(1,ultimo):
    numeros_primos(i)