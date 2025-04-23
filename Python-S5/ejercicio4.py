# Cálculo del consumo de combustible

while True:

    distancia_km = float(input("Ingresa la distancia recorrida en Km: "))
    litros_consumidos = float(input("Ingresa la cantidad de Litros de combustibles consumidos: "))
    if distancia_km == 0 and litros_consumidos == 0:
        print("Los valores no pueden ser igual a 0.")
        
    elif distancia_km < 0 or distancia_km < 0:
        print("Los valores no pueden ser menores a 0.")
    
    else: 
        break
        

rendimiento_kmL = distancia_km / litros_consumidos

precio_x_litro = float(input("Ingresa el precio de Combustible por litro: "))
while precio_x_litro <= 0:
    print("El precio por litro no puede ser igual o menor a 0. Intente Otra Vez.")
    precio_x_litro = float(input("Ingresa el precio de Combustible por litro: "))

total_combustible = litros_consumidos * precio_x_litro

print("\n")
print(f"Distancia Recorrida: {distancia_km: .2f}Km.")
print(f"Litros Consumidos: {litros_consumidos: .2f}L.")
print(f"Rendimiento del vehículo: {rendimiento_kmL: .2f}(Km/L).")
print(f"Gasto Total en Combustible: {total_combustible: .2f}$.")
