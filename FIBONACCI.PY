#FIBONACCI
print("INGRESA EL VALOR DEL NUMERO PARA EL CICLO")
x = int(input())
print ("")
num1=int(0)
num2=int(1)
resultado = num1+num2
print (resultado)
new_resultado = resultado + num2
print (new_resultado)
num1 = resultado
num2 = new_resultado
#Escribir "Este es el resultado anterior " Num1
#Escribir "Este es el resultado anterior " Num2
while resultado <= x:
    resultado=(num1 + num2)
    print (resultado)
#"Este es el resultado anterior " resultado
#"Este es el resultado anterior " NewResultado
    new_resultado = resultado + num2
    print (new_resultado)
    num1 = resultado
    num2 = new_resultado 
    
