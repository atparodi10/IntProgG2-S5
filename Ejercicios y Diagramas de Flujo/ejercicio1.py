# Verificar si un número está dentro de un rango válido

numero = int(input("Ingresa un número entre 100 y 999: "))

if numero < 100 or numero > 999:
    print(f"{numero} es Invalido.")

else:
    print(f"{numero} es Valido.")