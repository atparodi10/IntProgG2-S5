# Días de la semana

while True: 
    print("-----Seleccione Un día de la Semana-----")
    print("1. Lunes")
    print("2. Martes")
    print("3. Miércoles")
    print("4. Jueves")
    print("5. Viernes")
    print("6. Sábado")
    print("7. Domingo")
    print("\n")
    
    opcion = input("Ingrese su opción: ").strip()
    
    if opcion.isdigit():
        opcion = int(opcion)
        if 1 <= opcion <= 7:
            break
        
        else:
            print("Opción fuera de rango.")
    
    else:
        print("Ingresa un Número.")


if opcion == 1:
    print("Seleccionó Lunes.")

elif opcion == 2:
    print("Seleccionó Martes.")

elif opcion == 3:
    print("Seleccionó Miércoles.")
    
elif opcion == 4:
    print("Seleccionó Jueves.")
    
elif opcion == 5:
        print("Seleccionó Viernes.")
    
elif opcion == 6:
        print("Seleccionó Sábado.")

elif opcion == 7:
        print("Seleccionó Domingo.")
        

    