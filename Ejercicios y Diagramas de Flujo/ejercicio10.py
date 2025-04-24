# Verificación de validez de una fecha
while True:
    dia = (input("Ingresa el dia: ")).strip()
    if dia.isdigit():
        dia = int(dia)
        break
    print("Campo Vacío. Ingresa un dato valido.")
    
while True:
    mes = (input("Ingresa el mes (Por su nombre): ")).strip()
    if mes:
        break
    print("Campo Vacío. Ingresa un dato valido.")

while True:
    anio = (input("Ingresa el año: ")).strip()
    if anio:
        break
    print("Campo Vacío. Ingresa un dato valido.")


if mes.lower() == "febrero":
    if dia < 1 or dia > 28:
        print("Febrero no tiene ese dia")
    
    else:
        print(f"la fecha es: {dia} de {mes.capitalize()} del {anio}")

if mes.lower() == "abril" or mes.lower() == "junio" or mes.lower() == "septiembre" or mes.lower() == "noviembre":
    if dia < 1 or dia > 30:
        print(f"{mes.capitalize()} no tiene ese dia")
    
    else:
        print(f"la fecha es: {dia} de {mes.capitalize()} del {anio}")


if mes.lower() == "enero" or mes.lower() == "marzo" or mes.lower() == "mayo" or mes.lower() == "julio" or mes.lower() == "agosto" or mes.lower() == "octubre" or mes.lower() == "diciembre":
    if dia < 1 or dia > 31:
        print(f"{mes.capitalize()} no tiene ese dia")
    
    else:
        print(f"la fecha es: {dia} de {mes.capitalize()} del {anio}")

    