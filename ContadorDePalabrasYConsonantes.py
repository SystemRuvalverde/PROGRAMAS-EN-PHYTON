import re

def ContadorDeVocalYConsonante(texto):
    VocalesYConsonantes = re.findall('\w', texto)
    contador = {}
    
    for vocalYConsonante in VocalesYConsonantes:
        contador[vocalYConsonante] = contador.get(vocalYConsonante, 0) + 1
        
    return contador

#main
print ("Ingresa el texto")
texto = str(input())
ContadorDeVocalesYConsonantes = ContadorDeVocalYConsonante(texto)

for ContadorDeVocalYConsonante, contador in ContadorDeVocalesYConsonantes.items():
    print(f"{ContadorDeVocalYConsonante}: {contador}")
    if ContadorDeVocalYConsonante in ('a', 'e', 'i', 'o', 'u'):
        print("(vocal)")
    else:
        print ("(Consonante)")