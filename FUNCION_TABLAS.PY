import msvcrt

def esperar_tecla():
    msvcrt.getch()

def Tabla(num): #INICIO DE FUNCION TALBLA
    i=1
    print ("TABLA DEL "), num
    for i in range(1,11):
        print (num, " x ",i," = ", num*i) #TERMINA FUNCION TABLA
 #MAIN       
i=1
print ("PULSE CUALQUIER TECLA PARA ESCRIBIR TABLAS,")
esperar_tecla()
for i in range(1,5):
    Tabla(i)
    print (" ")
