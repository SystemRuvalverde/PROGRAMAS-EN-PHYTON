from datetime import datetime

def determinar_signo_zodiacal(fecha_nacimiento):
    # Convertir la cadena de fecha de nacimiento a un objeto datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

    # Obtener el día y el mes de la fecha de nacimiento
    dia = fecha_nacimiento.day
    mes = fecha_nacimiento.month

    # Determinar el signo zodiacal
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    else:
        return "Piscis"

# Ejemplo de uso
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")
signo_zodiacal = determinar_signo_zodiacal(fecha_nacimiento)
print(f"Tu signo zodiacal es {signo_zodiacal}.")