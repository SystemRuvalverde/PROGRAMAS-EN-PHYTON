#CAJERO
import sys

operacion = int()
saldo = int(0)
deposito = int(0)
respuesta = bool(True)
menu = True
def OPERACION_DEPOSITO():
    global saldo,deposito,respuesta
sys.exit()
def OPERACION_RETIRO(): #******************************************
    print("ESCRIBE LA CANTIDAD QUE DESEAS RETIRAR")
    retiro = int(input()) 
    print("TU RETIRO DE $",retiro," FUE HECHO CORRECTAMENTE")
    print("TU NUEVO SALDO ES DE $",saldo-retiro)
    print("DESEA CONTINUAR CON OTRA OPERACION??? ESCRIBIR Y / N")
    respuesta = bool(input())
    if respuesta == "N": 
            print ("NO SE CERRO SU SESION")
            print ("INGRESA NUEVAMENTE UNA OPCION VALIDA EN EL MENU")
            opcion=int(input())
    else: respuesta == "Y"
    print("VUELVA PRONTO")
    sys.exit()
	
def OPERACION_PAGO_LUZ(): #**********************************************
    print("PAGO DE LA LUZ: ESCRIBE LA CANTIDAD QUE VAS A PAGAR")
    pago_de_luz = int(input())
    print("TU PAGO DE LUZ DE $",pago_de_luz," FUE HECHO CORRECTAMENTE")
    print("TU NUEVO SALDO ES DE $", saldo - pago_de_luz)
    print ("DESEA CONTINUAR CON OTRA OPERACION??? ESCRIBIR Y / N")
    respuesta = bool(input())
    if respuesta == "N": 
            print ("NO SE CERRO SU SESION")
            print ("INGRESA NUEVAMENTE UNA OPCION VALIDA EN EL MENU")
            opcion=int(input())
    else: respuesta == "Y"
    print("VUELVA PRONTO")
    sys.exit()   
def OPERACION_PAGO_INTERNET(): #**********************************************
    print("PAGO DE LA INTERNET: ESCRIBE LA CANTIDAD QUE VAS A PAGAR")
    pago_de_internet = int(input())
    print("TU PAGO DE INTERNET DE $",pago_de_internet," FUE HECHO CORRECTAMENTE")
    print("TU NUEVO SALDO ES DE $", saldo - pago_de_internet)
    print("DESEA CONTINUAR CON OTRA OPERACION??? ESCRIBIR Y / N")
    respuesta = bool(input())
    if respuesta == "N": 
            print ("NO SE CERRO SU SESION")
            print ("INGRESA NUEVAMENTE UNA OPCION VALIDA EN EL MENU")
            opcion=int(input())
    else: respuesta == "Y"
    print("VUELVA PRONTO")
    sys.exit()  

  
def OPERACION_PAGO_TELEFONO(): #*************************************************
    print("PAGO TELEFONO: ESCRIBE LA CANTIDAD QUE VAS A PAGAR")
    pago_de_telefono = int(input())
    print("TU PAGO DE TELEFONO DE $",pago_de_telefono," FUE HECHO CORRECTAMENTE")
    print("TU NUEVO SALDO ES DE $", saldo - pago_de_telefono)
    print("DESEA CONTINUAR CON OTRA OPERACION??? ESCRIBIR Y / N")
    respuesta = bool(input())
    if respuesta == "Y": 
            print ("NO SE CERRO SU SESION")
            print ("INGRESA NUEVAMENTE UNA OPCION VALIDA EN EL MENU")
            opcion=int(input())
    else: respuesta == "N"
    print("VUELVA PRONTO")
    sys.exit()  

def OPERACION_PAGO_CABLE(): #****************************************************
    print("PAGO CABLE: ESCRIBE LA CANTIDAD QUE VAS A PAGAR")
    pago_de_cable = int(input())
    print("TU PAGO DE CABLE DE $",pago_de_cable," FUE HECHO CORRECTAMENTE")
    print("TU NUEVO SALDO ES DE $", saldo - pago_de_cable)
    print("DESEA CONTINUAR CON OTRA OPERACION??? ESCRIBIR Y / N")
    respuesta = bool(input())
    if respuesta == "Y": 
            print ("NO SE CERRO SU SESION")
            print ("INGRESA NUEVAMENTE UNA OPCION VALIDA EN EL MENU")
            opcion=int(input())
    else: respuesta == "N"
    print("VUELVA PRONTO")
    sys.exit()  
    

def OPERACION_SALDO_CUENTA(): #***************************************************   
    print ("ESTAS SEGURO QUE DESEAS CERRAR TU SESION??? (Y/N)")
    if respuesta.upper() == "N": 
        print ("NO SE CERRO SU SESION")
        print ("INGRESA NUEVAMENTE UNA OPCION VALIDA EN EL MENU")
        opcion=int(input())
    elif respuesta.upper() == "Y":
        print("VUELVA PRONTO")
        sys.exit() #PARA SALIR DEL PROGRAMA
    else:
        print("RESPUESTA NO VALIDA. INGRESA 'Y' PARA SI O 'N' PARA NO.")
    return True  # Indica que la sesión no se cerró

def OPERACION_CERRAR_SESION(): #***************************************************
        if operacion == 8:
            print("Estas seguro que deseas cerrar tu sesion (Y/N)")
            if respuesta == "N": 
                print("NO SE CERRO SU SESION")
                print("INGRESA NUEVAMENTE UNA OPCION VALIDA EN EL MENU")
            elif respuesta.upper() == "Y":
                print("VUELVA PRONTO")
                menu = False
                sys.exit() #PARA SALIR DEL PROGRAMA
        else:
            print("RESPUESTA NO VALIDA. INGRESA 'Y' PARA SI O 'N' PARA NO.")
            return True  # Indica que la sesión no se cerró
       
#MAIN ----- MENU DEL CAJERO
print ("1.- Deposito De Cuenta")
print ("2.- Retiro De Efectivo")
print ("3.- Pago De Luz")
print ("4.- Pago De Internet")
print ("5.- Pago De Telefono")
print ("6.- Pago De Cable")
print ("7.- Saldo De Cuenta")
print ("8.- Cerrar Sesion")
print ("Ingresa el numero de la operacion que desees realizar")
opcion=int(input())
if opcion == 1:
  OPERACION_DEPOSITO()
elif opcion == 2:
    OPERACION_RETIRO()
elif opcion == 3:
    OPERACION_PAGO_LUZ()
elif opcion == 4:
    OPERACION_PAGO_INTERNET()
elif opcion == 5:
    OPERACION_PAGO_TELEFONO()
elif opcion == 6:
    OPERACION_PAGO_CABLE()
elif opcion == 7:
    OPERACION_SALDO_CUENTA()
elif opcion == 8:
    if not OPERACION_CERRAR_SESION():
        sys.exit()
else:
    print ("OPCION NO VALIDA")
print ("TIEMPO AGOTADO")
print ("VUELVA PRONTO \(*u*)/ ")
menu = False
sys.exit()
    