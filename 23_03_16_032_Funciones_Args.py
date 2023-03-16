def colores(*args):
    print('El color ', args[1], ' es mi favorito. ', 'El color ',args[0], ' tampoco esta mal.')
    
colores("azul","amarillo")

def suma(*args):
    total = 0
    for x in args:
        total = total + x
    print("La suma de los numeros es: ",total)
    
suma(4,6,7,9,2)
#Tambien puede ser util para sumar varios numeros