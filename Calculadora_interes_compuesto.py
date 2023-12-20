import matplotlib.pyplot as plt

# Fórmula del interés compuesto: A = P(1 + r/n)^(nt)
    # A = Monto final
    # P = Monto principal (principal)
    # r = Tasa de interés anual (como decimal)
    # n = Número de veces que se compone el interés por año
    # t = Número total de años

def CalcularInteresCompuesto(inversion_inicial, taza_de_intereses, periodo):
    taza_interes = taza_de_intereses / 100.0
    monto_final = inversion_inicial * (1 + taza_interes/12.0)**(12.0 * periodo)
    return monto_final

def GenerarGrafica(inversion_inicial, taza_de_intereses, periodo):
    taza_interes = taza_de_intereses / 100.0
    montos = [inversion_inicial * (1 + taza_interes/12.0)**(12.0 * t) for t in range(periodo + 1)]
    
    plt.plot(range(periodo + 1), montos, marker='D')
    plt.xlabel('Monto_final')
    plt.ylabel('años')
    plt.title("Calculadora de interes compuesto")
    plt.grid(True)
    plt.show()

#main
inversion_inicial = int(input("Ingresa la inversion inicial: $"))
taza_intereses = float(input("Ingresa la taza de intereses: "))
periodo = int(input("Ingresa el periodo en años: "))

monto_final = CalcularInteresCompuesto(inversion_inicial, taza_intereses, periodo)
print(f"\nEl monto final despues de {periodo} años es de {monto_final:.2f}")

GenerarGrafica(inversion_inicial, taza_intereses, periodo)