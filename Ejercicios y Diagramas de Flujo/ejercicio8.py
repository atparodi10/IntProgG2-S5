# Verificación de inicio de sesión

while True:

    usuario = str(input("Ingresa tu usuario: ")).strip()
    if usuario:
        break
    print("Campo Vacío. Intenta Nuevamente.")

while True:
    contraseña = str(input("Ingresa tu Contraseña: ")).strip()
    if contraseña:
        break
    print("Campo Vacío. Intenta Nuevamente.")
    

if usuario == "admin" and contraseña == "1234admin":
    print("Acceso Permitido. Ingresando a su cuenta...")

else:
    print("Acceso Denegado.")