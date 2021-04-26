# Declaramos la clase.
class Rectangulo():
    # Tomamos las variables de declaración y las almacenamos en el objeto.
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Creamos el método para calcular el area, y hacemos que devuelva su valor
    def calc_area(self):
        area = self.base * self.altura
        return area

#Probamos creando un objeto Rectangulo, agregandole valores a su base y altura...
rectangulo1 = Rectangulo(1,2)

# y luego hacemos que calcule el area y que imprima el resultado.
print(rectangulo1.calc_area())

