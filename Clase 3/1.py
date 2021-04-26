#Pedimos al usuario dos valores.
#Lo convertimos de str a int.
try:
    a = int(input('Ingrese un valor a: '))
    b = int(input('Ingrese un valor b: '))
except ValueError:
    print('Error de valores, coloque un numero entero.')
else:
    #Hacemos el check, de pasarlo, imprimimos.
    if a > b:
        print('Hola Mundo')