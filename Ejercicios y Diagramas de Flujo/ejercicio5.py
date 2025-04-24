# Verificar si un número es par y es positivo


numero = int(input("Ingresa un numero: "))

if numero > 0 and numero % 2 == 0:
    print(f"{numero} es Positivo y es Par.")

elif numero < 0 and numero % 2 == 0:
    print(f"{numero} es Negativo y es Par.")

elif numero > 0 and numero % 2 == 1: 
    print(f"{numero} es Positivo y es Impar.")

else:
    print(f"{numero} es Negativo y es Impar.")