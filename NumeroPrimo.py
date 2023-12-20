def Primo(x):
    divisores=0
    i=1
    for i in range(1,x):
        if x%i==0:
            divisores=divisores+1
    if divisores==1:
        print ("El número ", x, " es primo")
    else:
        print ("El número ", x, " no es primo")

#main
i=0
ultimo=0
print ("¿Hasta que número quieres analizar?")
ultimo=int(input())
for i in range(1,ultimo):
    Primo(i)