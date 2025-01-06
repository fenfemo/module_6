class Animal():

    def __init__(self,name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self,food):
        if food.edible:
            self.fed = True
            print( f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')

class Mammal(Animal):
    pass
class Predator(Animal):
    pass

class Plant():

    def __init__(self,name, edible = False):
        self.name = name
        self.edible = edible

class Fruit(Plant):
    def __init__(self,name):
        self.edible = True
        self.name = name

class Flower(Plant):
    pass

a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')



print(a1.name)

print(p1.name)



print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)