def Validacion_de_correo(correo):
    return correo.endswith('@hotmail.com') or correo.endswith('@outlook.com') or correo.endswith('@gmail.com')
while True:
    correo = input("Ingresa un correo\n")
    if Validacion_de_correo(correo):
        print ("Acceso correcto")
        break
    else:
        print ("Incorrecto, intentelo de nuevo")