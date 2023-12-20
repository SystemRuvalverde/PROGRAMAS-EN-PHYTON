#print ("0")
Num1 = int(0)
Num2 = int(1)
Resultado = (Num1 + Num2)
print (Resultado) # 1

for Num1 in range(-1,150):
    while Resultado <= 100:
        Resultado = (Num1 + Num2)
        print (Resultado) # 3
        NewResultado = Resultado + Num2
        print (NewResultado)
        Num1 = Resultado
        Num2 = NewResultado  