#FORMULA DE IMC = PESO(KG)/(ESTATURA^2(MTS)

print("Ingresa tu peso(kg)")
peso = float(input())
print("Ingresa tu estatura(mts)")
estatura = float(input())
resultado = peso/(estatura*estatura)
print("TU INDICE DE MASA CORPORAL ES:", resultado )
if resultado < 18.5:
    print("TU PESO ES INFERIOR AL NORMAL")
elif resultado >= 18.5 and resultado < 24.9:
    print("TU PESO ES NORMAL")
elif resultado >= 25 and resultado < 29.9:
    print("TU PESO  ES SUPERIOR AL NORMAL")
elif resultado > 30:
    print("TU ESTAS BIEN PINCHE OBESO, GORDO, MARRANO Y PUERCO")
    print("PONTE A DIETA...!!! DE URGENCIA...!!!")