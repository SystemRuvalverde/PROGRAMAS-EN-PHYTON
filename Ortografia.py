palabras = ["serpiente", "zapato", "huevo", "hijo", "helicoptero", "avion", "Gimenez",
            "hola", "burro", "vaca"]

palabra = str(input("Escribe una palabra: "))
if palabra in palabras:
    print("la palabra es correcta")
else:
    print("tienes una falta de ortografia")