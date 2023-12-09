
def obtener_datos_usuario():
usuario = str()
apellido = str()
edad = str()
sexo = str()
print ("INGRESA EL NOMBRE DEL USUARIO")
usuario = input()
print ("INGRESA EL APELLIDO DEL USUARIO")
apellido = input()
print ("INGRESA EL EDAD DEL USUARIO")
edad = input()
print ("INGRESA EL SEXO DEL USUARIO")
sexo = input()
return {
        "Nombre": usuario,
        "Apellido": apellido,
        "Edad": edad,
        "Sexo" : sexo
}


#mylist = ["apple", "banana", "cherry"] #LISTA
#mytuple = ("apple", "banana", "cherry") #TUPLA
#myset = {"apple", "banana", "cherry"} #CONJUNTO
thisdict = obtener_datos_usuario()
print (thisdict)

thisdict = {  #DICCIONARIO
  "Nombre": usuario,
  "Apellido": apellido,
  "Edad": edad,
  "Sexo" : sexo
}
print (thisdict)