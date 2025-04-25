# Detección de condiciones extremas en servidor

while True:
    temperatura = input("Ingresa la temperatura del CPU (°C): ").strip()
    if temperatura.replace('.', '', 1).isdigit():
        temperatura = float(temperatura)
        break
    print("Dato inválido. Ingresa un número válido para la temperatura.")

while True:
    uso_cpu = input("Ingresa el uso del CPU(%): ").strip()
    if uso_cpu.replace('.', '', 1).isdigit():
        uso_cpu = float(uso_cpu)
        break
    print("Dato inválido. Ingresa un número válido para la temperatura.")

if temperatura > 80 or uso_cpu > 95:
    print("⚠️ CONDICIÓN CRÍTICA DETECTADA ⚠️")
    print(f"Temperatura del CPU: {temperatura: .2f}")
    print(f"Uso del CPU: {uso_cpu: .2f}")
    print("Iniando protocolo de emergencia...")

else:
    print(f"Temperatura del CPU: {temperatura: .2f}")
    print(f"Uso del CPU: {uso_cpu: .2f}")
    print("Condición estable. Las condiciones se encuentran dentro de los parámetros normales.")
        