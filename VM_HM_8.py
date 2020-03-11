class Turn(object):

    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items.pop(0)

    def empty(self):
        return len(self.items) == 0


turn = Turn()

turn.add_items(2)
turn.add_items(3)
turn.add_items(4)
print(turn.items)
turn.get_items()
print(turn.items)
turn.get_items()
print(turn.items)
print(turn.empty())



class Unit(object):
    __health = 100

    def __init__(self, armor, power, armdif=0, healdif=0):
        self.armor = armor
        self.power = power
        self.armdif = armdif
        self.healdif = healdif

    def health_down(self, dw):
        self.__health = self.__health - dw
        self.healdif = self.healdif + dw

    def heal(self):
        self.__health = self.__health + self.healdif

    def armor_down(self, uparm):
        self.armor = self.armor - uparm
        self.armdif = self.armdif + uparm

    def armor_return(self):
        self.armor = self.armor + self.armdif

    def power_up(self, uppow):
        self.power = self.power + uppow


hero1 = Unit(armor=50, power=10)

print(hero1.armor, hero1.power, hero1._Unit__health)
hero1.armor_down(15)
hero1.power_up(2)
hero1.health_down(15)
print(hero1.armor, hero1.power, hero1._Unit__health)
hero1.armor_down(15)
hero1.power_up(2)
hero1.health_down(15)
print(hero1.armor, hero1.power, hero1._Unit__health)
hero1.armor_return()
hero1.heal()
print(hero1.armor, hero1.power, hero1._Unit__health)

