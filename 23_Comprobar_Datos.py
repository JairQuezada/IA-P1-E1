color = ['verde', 'rojo', 'amarillo', 'morado1', 'naranja', 'negro', 'blanco', ' verde', 'rosa']

colo = input("Introduce un color. \n")
#Con el input se puede recibir una entrada del usuario en la consola

if colo in color:
    print("El color "+ colo + " esta admitido")
else:
    print("Color no admitido")
#La entrada del usuario se guarda y si algun color concuerda activa el if