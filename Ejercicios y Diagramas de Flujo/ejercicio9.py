#  Encontrar el mayor de tres números

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
num3 = int(input("Ingresa el tercer número entero: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} es el mayor.")

elif num2 > num1 and num2 > num3:
    print(f"{num2} es el mayor.")
    
else:
    print(f"{num3} es el mayor.")


