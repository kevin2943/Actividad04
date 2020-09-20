from math import pi


class Areas:

    @staticmethod
    def cuadrado(lado):
        return lado**2

    @staticmethod
    def triangulo(base, altura):
        return base*altura/2

    @staticmethod
    def circulo(radio):
        return pi*radio**2


lado = int(input("Introduzca la longitud del lado: "))
print("Area del Cuadrado {}\n".format(Areas.cuadrado(lado)))
base = int(input("Introduzca la base: "))
altura = int(input("Introduzca la altura: "))
print("Area del Triangulo {}\n".format(Areas.triangulo(base,altura)))
radio = int(input("Introduzca el radio: "))
print("Area del Circulo {}".format(Areas.circulo(radio)))
