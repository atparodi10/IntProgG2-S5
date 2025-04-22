# Control de inventario de un producto

inventario = int(input("Ingresa la cantidad inicial del inventario: "))
while inventario < 0:
    print("Ingresa una cantidad valida.")
    inventario = int(input("Ingresa la cantidad inicial del inventario: "))
    
productosRecibidos = int(input("Ingresa la cantidad de productos recibidos: "))
while productosRecibidos < 0:
    print("Ingresa una cantidad valida.")
    productosRecibidos = int(input("Ingresa la cantidad de productos recibidos: "))

sumaInventario = inventario + productosRecibidos

productosVendidos = int(input("Ingresa la cantidad de productos vendidos: "))
while productosVendidos < 0 or productosVendidos > sumaInventario:
    print("Ingresa una cantidad valida.")
    productosVendidos = int(input("Ingresa la cantidad de productos vendidos: "))

inventarioActual = sumaInventario - productosVendidos

print(f"Inventario Inical: {inventario}")
print(f"Productos recibidos: {productosRecibidos} Productos Vendidos: {productosVendidos:>3}")
print(f"Inventario Actual: {inventarioActual}")