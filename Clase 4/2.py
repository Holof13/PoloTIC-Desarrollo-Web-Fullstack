# Creamos la clase Vehículo, que va a tener de atributo la capacidad.
# Esta va a tener de valor default 6.
class Vehículo():
    def __init__(self, asientos = 6):
        self.asientos = asientos

# Creamos la clase Pasajero, los cuales solo van a estar definidos por su nombre.
# Esta clase al ser utilizada como objeto Str, va a devolver el nombre del pasajero.
class Pasajero():

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

# Creamos la clase Minibus, la cual toma de padre a la clase Vehículo
class Minibus(Vehículo):
    # Como atributos vamos a llamar a la clase padre usando super() para conseguir la cantidad de asientos
    # y dicho número es guardado como atributo de clase.
    # Tendremos a su vez el número del minibus y la lista de pasajeros como atributos.
    def __init__(self, numero):
        super().__init__(self)
        self.numero = numero
        self.pasajeros = []
    
    # Con el método capacidad, sobreescribimos el valor de asientos dado por la clase Vehiculo.
    def capacidad(self, capacidad_total):
        self.asientos = capacidad_total
    
    # Este metodo nos devuelve la resta entre la cantidad total de asientos y la cantidad de pasajeros en la lista.
    def disponibilidad(self):
        return self.asientos - len(self.pasajeros)
   
    # Este metodo toma de atributo un objeto pasajero.
    def subir_pasajero(self, pasajero : Pasajero):
        # Primero checkeamos si el pasajero ya esta en el minibus.
        if pasajero in self.pasajeros:
            print('Ya hay un pasajero con ese nombre en el minibus')

        # Luego si hay lugar en el minibus para el pasajero, de ser así es agregado a la lista.
        elif len(self.pasajeros) < self.asientos:
            self.pasajeros.append(pasajero)
            print(f'{pasajero}, subió al Minibus N°{self.numero}')
        
        # De lo contrario, mostramos que no fue posible, usando el metodo __str__ del objeto pasajero para mostrar su nombre.
        else:
            print(f'Pasajero: {pasajero} no subió al minibus, capacidad maxima alcanzada.')

#### TEST ####
# Generamos una lista de pasajeros
lista = ['Agustin', 'Pichi', 'Ricky', 'Vara', 'Nico']
# y un objeto minibus
minibus1 = Minibus(1)
# el cual tiene una capacidad máxima de 4 para hacer el ejemplo mas simple, en realidad tendria que ser 50.
minibus1.capacidad(4)

# Por cada potencial pasajero en la lista...
for nombre in lista:
    # mostramos la capacidad disponible...
    print(f'Disponibilidad: {minibus1.disponibilidad()}')
    # sobreescribimos el nombre del pasajero, por un objeto Pasajero con el mismo nombre como atributo...
    nombre = Pasajero(nombre)
    # y por último tratamos de subir a este al minibus.
    minibus1.subir_pasajero(nombre)
