# Cálculo del consumo de agua por persona
while True: 
    litros_consumidos = float(input("Ingresa la cantidad de Litros de Agua consumidos en un mes: "))
    cantidad_de_personas = int(input("Ingresa la cantidad de personas que viven en la casa: "))
    
    if litros_consumidos == 0 and cantidad_de_personas == 0:
        print("Se está indicando que no existe un consumo existente. Ingrese valores Mayores a 0.")
    
    elif litros_consumidos < 0  or cantidad_de_personas < 0:
        print("Los valores no pueden ser menores a 0.")
    
    else:
        break

consumo_mensual_x_persona = litros_consumidos / cantidad_de_personas

consumo_diario_x_persona = consumo_mensual_x_persona / 30

print("\n")
print("-"*20,"REPORTE DE CONSUMO DE AGUA","-"*20)
print(f"Consumo Total en un Mes:{litros_consumidos: .2f}L \tCantidad de Personas en la Vivienda: {cantidad_de_personas} \nConsumo Mensual por Persona:{consumo_mensual_x_persona: .2f}L \tConsumo Diario por Persona:{consumo_diario_x_persona: .2f}L")

    