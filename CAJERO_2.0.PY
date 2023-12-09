import sys
operacion = int(0)
saldo = int(0)
deposito = int(0)
respuesta = bool(True)
retiro = int(0)
# This function is responsible for performing a deposit operation.
def OPERACION_DEPOSITO():
    global saldo,deposito, retiro
    print("DEPOSITO DE CUENTA")
    deposito = int(input("INGRESE EL MONTO A DEPOSITAR: $"))
    #saldo = saldo + deposito
    print("TU NUEVO SALDO ES DE $",saldo+deposito)
    OPERACION_MENU()

# This function is responsible for performing a withdrawal operation.
def OPERACION_RETIRO():
    print("RETIRO DE EFECTIVO")
    retiro = int(input("INGRESE EL MONTO A RETIRAR: $"))
    print("TU NUEVO SALDO ES DE $", saldo-retiro)
    OPERACION_MENU()

# This function is responsible for performing a payment for electricity.
def OPERACION_PAGO_LUZ():
    print("PAGO DE LUZ")
    pago_de_luz = int(input("INGRESE EL MONTO A PAGAR: $"))
    print("TU NUEVO SALDO ES DE $", saldo - pago_de_luz)
    OPERACION_MENU()

# This function is responsible for performing a payment for internet.
def OPERACION_PAGO_INTERNET():
    print("PAGO DE INTERNET")
    #saldo = saldo 
    pago_de_internet = int(input("INGRESE EL MONTO A PAGAR: $"))
    print("TU NUEVO SALDO ES DE $", saldo - pago_de_internet)
    OPERACION_MENU()

# This function is responsible for performing a payment for telephone.
def OPERACION_PAGO_TELEFONO():
    print("PAGO DE TELEFONO")
    #saldo = saldo
    pago_de_telefono = int(input("INGRESE EL MONTO A PAGAR: $"))
    print("TU NUEVO SALDO ES DE $",  saldo - pago_de_telefono)
    OPERACION_MENU()

# This function is responsible for performing a payment for cable TV.
def OPERACION_PAGO_CABLE():
    print("PAGO DE CABLE")
    #saldo = saldo
    pago_de_cable = int(input("INGRESE EL MONTO A PAGAR: $"))
    print("TU NUEVO SALDO ES DE $", saldo = pago_de_cable)
    OPERACION_MENU()

# This function is responsible for checking the account balance.
def OPERACION_SALDO_CUENTA():
    print("SALDO DE CUENTA")
    print("TU SALDO ACTUAL ES DE $", saldo)
    OPERACION_MENU()

# This function is responsible for closing the session.
def OPERACION_CERRAR_SESION():
    while True:
        cerrar_sesion = input("DESEA CERRAR SESION? Y/N: ").upper()
        if cerrar_sesion == 'Y':
            print("VUELVA PRONTO")
            menu = False
            sys.exit() # To exit the program
        elif cerrar_sesion == 'N':
            return False # Indicates that the session was not closed
        else:
            print("RESPUESTA NO VALIDA. INGRESA 'Y' PARA SI O 'N' PARA NO.")
    return True # Indicates that the session was not closed

# This function displays the menu for the user to select an operation.
def OPERACION_MENU():
    #while opcion == 9:
        print("\n1.- Deposito De Cuenta")
        print("2.- Retiro De Efectivo")
        print("3.- Pago De Luz")
        print("4.- Pago De Internet")
        print("5.- Pago De Telefono")
        print("6.- Pago De Cable")
        print("7.- Saldo De Cuenta")
        print("8.- Cerrar Sesion")
        try:
            opcion = int(input("SELECCIONE UNA OPCION: "))
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
                menu = OPERACION_CERRAR_SESION()
            else:
                print("OPCION NO VALIDA")
        except ValueError:
            print("VALOR NO VALIDO. INGRESE UN NUMERO DEL 1 AL 8.")
    #menu = False
# Main function
#def main():
print("* B I E N V E N I D O *")
print("* * * * * A L * * * * *")
print("* * * C A J E R O * * *")
saldo = 0
OPERACION_MENU()

# Run the program
#if __name__ == "__main__":
    #main()