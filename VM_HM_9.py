import random


class Fighter(object):
    max_health = 100
    max_armor = 50

    def __init__(self, name, health, armour, power):

        self.name = name
        self.__health = health
        self.armour = armour
        self.power = power
        self.currenthealth = health

        self.equipments = []

    def put_on(self, equipment):

        if equipment in self.equipments:
            raise Exception

        self.armour = self.armour + equipment.armour
        self.power = self.power + equipment.power

        self.equipments.append(equipment)

    def remove(self, equipment):

        if equipment in self.equipments:
            self.armour = self.armour - equipment.armour
            self.power = self.power - equipment.power

            self.equipments.remove(equipment)
        else:
            raise Exception

    def get_health(self):
        return self.__health

    def set_health(self, value):
        if value > self.max_health:
            self.__health = self.max_health

    health = property(get_health, set_health)

    def get_armor(self):
        return self.__armor

    def set_armor(self, value):
        if value > self.max_armor:
            self.__armor = self.max_armor

    armor = property(get_armor, set_armor)

    def heal(self):
        self.__health = self.max_health
        return self.__health


class Equipment(object):

    def __init__(self, _type, power, armour):
        self._type = _type
        self.power = power
        self.armour = armour


class Fight(object):

    @staticmethod
    def fight(first_fighter, second_fighter):
        while first_fighter.currenthealth > 0 and second_fighter.currenthealth > 0:
            choise = random.choice([0, 1])
            if choise == 0:
                first_fighter.currenthealth -= second_fighter.power
            elif choise == 1:
                second_fighter.currenthealth -= first_fighter.power

        if first_fighter.currenthealth > 0:
            del second_fighter
            return first_fighter
        # Ранндомная битва

        else:
            del first_fighter
            return second_fighter


class FighterFirstRang(Fighter):
    max_health = 100
    rang_f = 0

    def put_on(self, equipment):
        if len(self.equipments) >= 2:
            del self.equipments[0]
            self.equipments.append(equipment)

        super().put_on(equipment)


class FighterSecondRang(Fighter):
    rang_f = 1
    max_health = 100

    def put_on(self, equipment):
        if len(self.equipments) > 1:
            del self.equipments[0]
            self.equipments.append(equipment)

        super().put_on(equipment)


class FighterThirtRang(Fighter):
    rang_f = 2
    max_health = 100
    max_armor = 10

    def put_on(self, equipment):
        raise Exception("low rang")


fighter_1 = FighterFirstRang("Fighter 1", 100, 30, 30)
fighter_2 = FighterFirstRang("Fighter 2", 100, 30, 30)
if fighter_1.rang_f == fighter_2.rang_f:  # Проверка соотвествия рангов
    shield = Equipment('shield', -3, 2)
    sword = Equipment('sword', 10, -5)

    fighter_1.put_on(shield)
    fighter_2.put_on(shield)

    fight = Fight()

    winner = fight.fight(fighter_1, fighter_2)

    print(winner.name)
else:
    raise Exception("differents rangs")

fighter_1 = FighterFirstRang("Fighter 1", 10, 30, 30)
print(fighter_1.health)
fighter_1.heal()  # Лечение бойца
print(fighter_1.health)
