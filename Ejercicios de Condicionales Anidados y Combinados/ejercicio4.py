# determinar si tres medidas pueden formar un triángulo

def es_triangulo(lado1, lado2, lado3):
    suma = lado1 + lado2
    
    if suma > lado3:
        return "Es un triángulo."
    
    else:
        return "No es un triángulo."     


def main():
    print("Ingresa los siguientes valores: ")
    print("="*30)
    
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))
    print (es_triangulo(lado1, lado2, lado3))

main()