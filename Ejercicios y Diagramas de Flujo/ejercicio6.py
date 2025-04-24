# Evaluar si un estudiante aprueba o reprueba

while True: 
    calificacion = float(input("Ingresa tu calificación (0-100): "))
    
    if calificacion < 0 or calificacion > 100:
        print("Ingresa una calificacion valida. Entre 0 a 100.")
    
    elif calificacion > 70:
        print(f"Aprobado con una nota de {calificacion: .2f}.")
        break
    
    else:
        print(f"Reprobado con una nota de {calificacion: .2f}.")
        