class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


r1 = Rectangle(2, 4)


class Square(Rectangle):

    # Aqui ele vai herdar o init de retangulo e substituir os parametros de set iniciais para lados

    def __init__(self, length):
        super().__init__(length, length)


sq1 = Square(4)


class Cube(Square):

    # Aqui ele vai herdar quadradado
    # e ainda criar novos métodos como área da superfície

    def surface_area(self):
        return self.area() * 6

    def volume(self):
        return super().area() * self.length


cubo1 = Cube(3)

print(cubo1.surface_area())
print(cubo1.volume())
