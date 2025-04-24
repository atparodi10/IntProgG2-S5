# Notificación de velocidad peligrosa en carretera

while True: 
    velocidad = float(input("Ingresa la velocidad actual: "))

    if velocidad <= 0:
        print("Estas detenido, o ¿En retroceso?. Ingresa la velocidad nuevamente.")
    
    elif velocidad > 120:
        print("¡Reduzca la Velocidad!")
        break
        
    else:
        print("Velocidad permitida.")
        break