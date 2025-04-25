# Sueldo de empleado y calculo de bono

while True:
    sueldo = float(input("Ingrese su sueldo: "))
    if sueldo <= 0:
        print("Su sueldo no puede ser menor o igual a 0. Intente Nuevamente.")
    
    else: 
        if sueldo > 3000:
            bono = 0.10
        
        elif sueldo <= 3000 and sueldo > 1500:
            bono = 0.05
        
        else:
            bono = 0
            print("Ya que su sueldo es menor a 1500$ no tendrá bono.")
        break

total = sueldo * bono
sueldo_total = sueldo + total

print("\n")
print(f"Sueldo: {sueldo: .2f}$")
print(f"Bono: {total: .2f}$")
print(f"Sueldo con el Bono: {sueldo_total: .2f}$")