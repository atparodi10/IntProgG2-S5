# Detectar si un usuario está inactivo por más de 30 días

from datetime import datetime

fecha_usuario = input("Ingresa la fecha de su ultimo inicio de sesión (dd/mm/aaaa): ")
fecha_usuario = datetime.strptime(fecha_usuario, "%d/%m/%Y")
fecha_actual = datetime.today()

dias_de_diferencia = (fecha_actual - fecha_usuario).days

if dias_de_diferencia > 30:
    print(f"Cuenta Inactiva. Ultima Sesión registrada hace {dias_de_diferencia} días.")

else:
    print(f"Cuenta Activa. Ultima Sesión registrada hace {dias_de_diferencia} días.")