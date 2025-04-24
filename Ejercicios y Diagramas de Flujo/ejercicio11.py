# Determinar si hay saldo suficiente para una compra

precio = float(input("Ingresa el precio del producto: "))

while precio <= 0:
    print("El precio no peude ser menor a 0.")
    precio = float(input("Ingresa el precio del producto: "))


while True:
    saldo_disponible = float(input("Ingresa tu saldo disponible: "))
    if saldo_disponible < 0:
        print("El saldo disponible no puede ser menor a 0.")
    
    elif saldo_disponible == 0:
        print("No tiene dinero disponible.")
        break
    
    else:
        break

if saldo_disponible >= precio:
    print(f"Saldo Disponible: {saldo_disponible: .2f}")
    print(f"Precio del producto: {precio: .2f}")
    print("La compra está permitida.")
    total = saldo_disponible - precio
    print(f"Dinero Restante luego de la compra: {total: .2f}")
    

else:
    print("\n")
    print(f"Saldo Disponible: {saldo_disponible: .2f}")
    print(f"Precio del producto: {precio: .2f}")
    print("La compra no está permitida.")