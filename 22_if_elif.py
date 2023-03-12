edad = int(input("Cual es su edad?\n"))

if edad <=0:
    print('nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
    print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
    print('Eres una adulto joven.')
elif edad > 45 and edad <= 100:
    print('Eres un adulto mayor.')
elif edad > 100 and edad <= 120:
    print('Wow, es muy viejo.')
else:
    print('Edad no valida.')