lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# Iteramos por cada item en la lista
for x in lista1:
    # Verificamos que el número sea menor que 150, de ser así paramos la iteración y mostramos un mensaje.
    if x > 150:
        print(f'{x} es mas grande que 150. Cerrando programa.')
        break
    # Ahora verificamos que el número sea múltiplo de 5. Cuando esto sucede, el resto de la división entre
    # el número y 5 es 0. De ser así, mostramos el número y continuamos iterando.
    elif x % 5 == 0 :
        print(x)

    
