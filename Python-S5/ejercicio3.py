# Cálculo de interes compuesto

capital_inicial = float(input("Ingresa el capital inicial: "))
while capital_inicial <= 0:
    print("El capital no puede ser igual o menor a 0.")
    capital_inicial = float(input("Ingresa el capital inicial: "))

interes_anual = float(input("Ingresa el interes anual a aplicar: "))
while interes_anual < 0:
    print("El interes anual no puede tener un equivalente a menos 0%")
    interes_anual = float(input("Ingresa el interes anual a aplicar: "))

porcentaje_interes = interes_anual / 100

tiempo_de_prestamo = int(input("Ingresa los años los cuales se va a llevar a cabo el préstamo: "))

monto_final = ((1 + porcentaje_interes) ** tiempo_de_prestamo) * capital_inicial
interes_ganado = monto_final - capital_inicial

print("-"*5,"REPORTE""-"*5)
print(f"Capital Inicial: {capital_inicial: .0f}") 
print(f"Tasa de Interes Anual: {interes_anual}%")
print(f"Años los cuales se lleva a cabo el préstamo: {tiempo_de_prestamo}")
print(f"Monto Final: {monto_final:.2f}")
print(f"Interes Ganado: {interes_ganado:.2f}")
print("-"*20)
