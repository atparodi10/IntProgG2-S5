# Calificacion de un estudiante (de 0-10)

while True:
    nota = float(input("Ingresa su calificación(0-10): "))
    
    if nota < 0 or nota > 10:
        print("Ingresa una nota Valida.")
    
    else:
        if nota >= 0 and nota < 3:
            print(f"{nota: .2f} = F.")

        elif nota > 2 and nota < 5:
            print(f"{nota: .2f} = D.")

        elif nota > 4 and nota < 7:
            print(f"{nota: .2f} = C.")

        elif nota > 6 and nota < 9:
            print(f"{nota: .2f} = B.")
            
        else:
            print(f"{nota: .2f} = A")
        break

