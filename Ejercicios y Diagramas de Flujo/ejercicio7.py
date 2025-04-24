# Cálculo de propina según satisfacción

monto_total = float(input("Ingrese el monto total de la cuenta: "))
while monto_total <= 0:
    print("Ingresa un monto valido para el total de la cuenta.")
    monto_total = float(input("Ingrese el monto total de la cuenta: "))

while True:
    nivel_satifaccion = input("Ingresa tu nivel de Satisfacción (buena o mala): ").strip()
    if nivel_satifaccion:
        break
    print("Campo Vacío. Intente nuevamente.")

if nivel_satifaccion.lower() == "buena":
    propina = 0.15

elif nivel_satifaccion.lower() == "mala":
    propina = 0.05

else: 
    print("Nivel de satisfacción no reconocido. Se aplicará el 10% de propina.")
    propina = 0.10

propina = monto_total * propina
cuenta_total = propina + monto_total

print("-"*5,"FACTURA","-"*5)
print(f"Monto Total: {monto_total: .2f}")
print(f"Nivel de Satisfacción: {nivel_satifaccion}")
print(f"Propina: {propina: .2f}")
print(f"Cuenta Total: {cuenta_total: .2f}")
print("-"*20)
