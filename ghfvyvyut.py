def CalcularFrecuenciaCardiacaMaxima(edad):
    return 220 - edad

def FrecuenciaCardiacaReserva(frecuencia_cardiaca_maxima, frecuencia_cardiaca_reposo):
    return frecuencia_cardiaca_maxima - frecuencia_cardiaca_reposo

# Main
edad = int(input("Ingresa tu edad: "))
frecuencia_cardiaca_reposo = int(input("Ingresa tus pulsaciones en reposo: "))

frecuencia_cardiaca_maxima = CalcularFrecuenciaCardiacaMaxima(edad)
print(f"La frecuencia cardiaca maxima es: {frecuencia_cardiaca_maxima}")

frecuencia_cardiaca_reserva = FrecuenciaCardiacaReserva(frecuencia_cardiaca_maxima, frecuencia_cardiaca_reposo)
print(f"La frecuencia cardiaca de reserva es: {frecuencia_cardiaca_reserva}")

# Porcentajes como decimales (0.50, 0.55, 0.60, 0.65, 0.70)
porcentaje_intensidad = (0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.90, 0.95)
porcentaje_trabajo_frecuencia_cardiaca_reserva = [porcentaje * frecuencia_cardiaca_reserva for porcentaje in porcentaje_intensidad]
print (f"el porcentaje de trabajo de la frecuencia cardiaca de reserva es: {porcentaje_trabajo_frecuencia_cardiaca_reserva}")

frecuencia_cardiaca_trabajo = [frecuencia + frecuencia_cardiaca_reposo for frecuencia in porcentaje_trabajo_frecuencia_cardiaca_reserva]
print(f"La frecuencia cardiaca del trabajo es: {frecuencia_cardiaca_trabajo}")
