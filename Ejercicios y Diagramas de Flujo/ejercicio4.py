#  Validar edad mínima para votar

while True:
    edad = int(input("Ingresa tu edad: "))
    if edad <= 0:
        print("Ingresa una edad mayor a 0.")
    
    elif edad >= 18:
        print("Puede Votar.")
        break

    else: 
        print("No puede Votar.")
        break
    
