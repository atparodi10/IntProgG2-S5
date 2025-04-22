calificacion1 = int(input("Ingresa la calificacion 1: "))
calificacion2 = int(input("Ingresa la calificacion 2: "))
calificacion3 = int(input("Ingresa la calificacion 3: "))

suma = calificacion1 + calificacion2 + calificacion3
promedio = suma / 3

print(f"""Calificación 1: {calificacion1:>3}  Calificación 2: {calificacion2:>3}  Calificación 3: {calificacion3:>3}  Promedio: {promedio:<15}{promedio:>.0f}""")