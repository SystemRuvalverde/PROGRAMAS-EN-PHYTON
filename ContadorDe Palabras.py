import re

def ContadorDePalabra(texto):
    palabras = re.findall('\w+', texto)
    contador = {}
    
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
        
    return contador

print ("Ingresa el texto")
texto = str(input())
ContadorDePalabras = ContadorDePalabra(texto)

for palabra, contador in ContadorDePalabras.items():
    print(f"{palabra}: {contador}")
