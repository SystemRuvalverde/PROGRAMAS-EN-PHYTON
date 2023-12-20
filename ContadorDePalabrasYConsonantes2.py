# Texto de entrada
texto = input("Escribe un texto: ")

# Variables para almacenar el conteo de vocales y consonantes
contador_vocales = 0
contador_consonantes = 0

# Convierte el texto a minúsculas para evitar errores de distinción
texto = texto.lower()

# Recorre cada carácter del texto
for letra in texto:
    # Si el carácter es una vocal
    if letra in ('a', 'e', 'i', 'o', 'u'):
        contador_vocales += 1
    # Si el carácter es una consonante
    else:
        letra.isalpha()
        contador_consonantes += 1
        
# Imprime el conteo de vocales y consonantes
print("Vocales: ", contador_vocales)
print("Consonantes: ", contador_consonantes)
