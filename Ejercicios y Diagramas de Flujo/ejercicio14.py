edad = int(input("Ingresa tu edad: "))


if edad >= 0 and edad < 12:
      print("Eres un niño")
    
elif edad >= 12 and edad < 18:
    print("Eres Adolescente.")
    
elif edad >= 18 and edad < 65:
    print("Eres un adulto.")

elif edad >= 65:
    print("Eres un adulto mayor.")
  

else:
    print("Ingresa una Edad valida.")