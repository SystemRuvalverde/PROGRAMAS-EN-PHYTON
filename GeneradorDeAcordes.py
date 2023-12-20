import random

def Acordes_musicales():
    notas = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    tonica = random.choice(notas)
    
    acorde = [tonica]
    acorde.append(notas[(notas.index(tonica) + 4) % 12])
    acorde.append(notas[(notas.index(tonica) + 7) % 12])
    return acorde

acorde_generado = Acordes_musicales()
print ("Acorde generado:", acorde_generado)