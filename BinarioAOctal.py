import math

def BinAOct(binario):
    pos=0 #Para ir recorriendo los digitos del número
    result=0
    dig=0 #Para ir guardando los digitos del número
    while binario>0:
        dig=binario%10 #Saco el dígito
        result=result+dig*(2**(pos)) #Opero
        pos=pos+1 #Incrementar posición
        binario=math.trunc(binario/10)
    return result

#Función para convertir de decimal a octal
def ConversorDesdeDecimal(num):
    resultado = ""
    digito = ""
    cociente = ""
    if num==0:
        resultado = "0"
    while num>0:
        cociente = (num%8)
        digito = str(cociente)
        resultado = digito + resultado
        num = math.trunc(num/8)
    return resultado

#Función para convertir de decimal a binario
        
#main
binario=0
octal=""
decimal=0
print ("Dime el valor del número binario que quieres convertir a octal")
binario = int(input())
decimal=BinAOct(binario)
octal=ConversorDesdeDecimal(decimal)
print ("OCTAL: ", octal)    

"""

Algoritmo ConvertirBinarioAOctal
	Definir binario,decimal Como Entero;
	Definir octal como Cadena;
	binario=0;
	octal="";
	decimal=0;
	Escribir "Dime el valor del número binario que quieres convertir a octal";
	Leer binario;
	decimal=BinADec(binario);
	octal=ConversorDesdeDecimal(decimal);
	Escribir "OCTAL: ", octal;
FinAlgoritmo
"""