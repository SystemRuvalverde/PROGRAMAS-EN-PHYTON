import random

def choose_word():
    palabras = ["python", "programacion", "inteligencia", "artificial", "openai", "ahorcado"]
    return random.choice(palabras)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    intentos_maximos = 6
    palabra_secreta = choose_word()
    letras_adivinadas = []
    intentos_realizados = 0

    print("¡Bienvenido al juego del ahorcado!")
    print(display_word(palabra_secreta, letras_adivinadas))

    while True:
        guess = input("Adivina una letra: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in letras_adivinadas:
                print("Ya has adivinado esa letra. Intenta de nuevo.")
            elif guess in palabra_secreta:
                letras_adivinadas.append(guess)
                print("¡Correcto!")
            else:
                intentos_realizados += 1
                print("Incorrecto. Te quedan {} intentos.".format(intentos_maximos - intentos_realizados))
        else:
            print("Ingresa una letra válida.")

        print(display_word(palabra_secreta, letras_adivinadas))

        if all(letter in letras_adivinadas for letter in palabra_secreta):
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

        if intentos_realizados == intentos_maximos:
            print("¡Oh no! Has agotado tus intentos. La palabra era '{}'.".format(palabra_secreta))
            break

if __name__ == "__main__":
    hangman()