# Creamos una lista vacía para almacenar los números.
numeros = []
# Iteramos 5 veces...
for i in range(0,5):
    # y pedimos input del usuario, lo convertimos de str a float.
    # Con cada una de estas inputs, se agregan a la lista.
    # Para el prompt de la input, usamos el numero de iteración + 1 para preguntar por el número.
    numeros.append(float(input(f'N°{i + 1 } = ')))
# Mostramos la lista al usuario, iterando por cada item en la lista.
for x in numeros:
    print(x)
