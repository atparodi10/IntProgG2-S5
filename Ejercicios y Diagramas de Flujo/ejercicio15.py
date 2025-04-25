# Simulador de sistema de puntuación de conducta

puntos = input("Ingresa tus puntos (de 0 a 10): ")

try:
    puntos = float(puntos)

    if puntos < 0 or puntos > 10:
        print("Error: El valor debe estar entre 0 y 10.")
    elif puntos >= 9:
        print("Excelente")
    elif puntos >= 7:
        print("Bueno")
    elif puntos >= 5:
        print("Regular")
    else:
        print("Deficiente")
        
except ValueError:
    print("Error: Ingresa un número válido.")
