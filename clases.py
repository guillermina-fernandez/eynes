import math


class Circulo(object):
    def __init__(self, radio):
        self.radio = radio
        if self.radio <= 0:
            raise Exception('Intente nuevamente. El radio ingresado debe ser mayor a cero.')

    def area(self):
        print(f'El área de un círculo de radio {self.radio} es {math.pi * (self.radio ** 2)}')

    def perimetro(self):
        print(f'El perímetro de un cículo de radio {self.radio} es {math.pi * (2 * self.radio)}')

    def __mul__(self, number):
        if number <= 0:
            raise Exception('Intente nuevamente. El número por el cual multiplicar el círculo debe ser mayor que cero.')
        else:
            print(Circulo(self.radio * number))


Circulo(8).area()
Circulo(5).perimetro()
Circulo(4) * 3
