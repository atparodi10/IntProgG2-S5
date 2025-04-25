# Menú de operaciones bancarias


saldo_inicial = float(input("Ingresa tu saldo: "))
while saldo_inicial < 0:
    print("Tu saldo no puede ser menor a 0.")
    saldo_inicial = float(input("Ingresa tu saldo: "))


print("-----OPERACIONES BANCARIAS-----")
print("1. Vaciar Cuenta")
print("2. Depositar")
print("3. Retirar")

while True:
    opcion = input("Ingrese su opcion: ").strip()
    if opcion.isdigit():
        opcion = int(opcion)
        break
    print("Campo Vacío o Ingresa un dato valido.")

if opcion == 1:
    print("-----VACIAR CUENTA-----")
    print(f"Saldo: {saldo_inicial:.2f}$")
    print(f"Vaciando Cuenta...")
    vaciar_cuenta = saldo_inicial - saldo_inicial
    print(f"Saldo despues de la operacion: {vaciar_cuenta: .2f}")

elif opcion == 2:
    print("-----DEPOSITAR-----")
    print(f"Saldo: {saldo_inicial:.2f}$")
    deposito = float(input("Ingresa la cantidad a depositar: "))
    while deposito <= 0:
        print("Ingrese una cantidad valida a depositar.")
        deposito = float(input("Ingresa la cantidad a depositar: "))
        
    deposito_cuenta = saldo_inicial + deposito
    print(f"Saldo despues de la operacion: {deposito_cuenta: .2f}")

elif opcion == 3:
    print("-----RETIRAR-----")
    print(f"Saldo: {saldo_inicial:.2f}$")
    retirar = float(input("Ingresa la cantidad a retirar: "))
    while retirar > saldo_inicial or retirar <= 0:
        print("Ingrese una Cantidad Valida.")
        retirar = float(input("Ingresa la cantidad a retirar: "))
        
    retiro_cuenta = saldo_inicial - retirar
    print(f"Saldo despues de la operacion: {retiro_cuenta: .2f}")

else:
    print("Opcion no valida.")
    print("Saliendo de la operacion...")

