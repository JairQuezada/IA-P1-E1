edad = int(input("Cual es su edad?\n"))
#Con el input se puede meter un dato desde la terminal
if edad <=0:
    print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
    print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
    print('Eres un adulto.')
elif edad > 45 and edad <= 100:
    print('Eres un adulto mayor.')
elif edad > 100 and edad <= 120:
    print('Eres muy mayor.')
else:
    print('Edad no valida.')
#El elif sirve para una lista de opciones, si no se cumple ninguna se salta al else