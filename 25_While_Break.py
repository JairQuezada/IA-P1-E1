x=0
while x < 40:
    x += 1
    if x == 4 or x==6 or x==10:
        print("Se salto el valor "+ str(x))
        continue
    if x == 20:
        print("Se rompio la ejecucion del bucle cuando x valia " + str(x))
        break
    print("El valor del bucle es: " + str(x))