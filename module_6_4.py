import math
from email.policy import default


class Figure:

    sides_count = 0

    def __init__(self, __color, __sides):
        self.filled = True
        self.__sides = __sides
        self.__color = __color

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        r += self.__color[0]
        g += self.__color[1]
        b += self.__color[2]
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        return r in range(256) and g in range(256) and b in range(256)

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            for i in args:
                # print(type(i)) # <class 'tuple'> хотелось бы  узнать почему так?
                i = i[0]
                # print(type(i)) # <class 'int'>
                if (isinstance(i, int) and i > 0):
                    return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *args):
        if self.__is_valid_sides(args):
            self.__sides = list(args)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        default_side = 1
        if len(sides) == 1:
            default_side = sides[0]
        self.__radius = default_side / (2 * math.pi)
        super().__init__(color, default_side)


    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):

    def __init__(self, color, *sides):
        default_sides = (1, 1, 1)
        if len(sides) == 3:
            default_sides = sides
        super().__init__(color, default_sides)

    def get_square(self):
        p = len(self) / 2
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        square = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return square

class Cube(Figure):

    def __init__(self,color, *sides):
        default_sides = []
        side = 1
        if len(sides) == 1:
            side = sides[0]
        for i in range(12):
            default_sides.append(side)
        super().__init__(color, default_sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
circle1.set_sides(1010)
print(circle1.get_sides())

triangle1 = Triangle((200, 200, 200), 5, 5, 9)
print(triangle1.get_square())

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

