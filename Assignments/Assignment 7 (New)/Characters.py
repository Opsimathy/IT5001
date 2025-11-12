from random import randint
from Team import *

print_action_description = True


def dprint(s):
    if print_action_description:
        print(s)


# Constants for Mage Type
mana_cost = 20
mana_recovery = 30


class Character(object):
    def __init__(self):
        self.name = ''
        self.max_hp = 1000
        self.hp = 1000
        self.str = 0
        self.maxmana = 0
        self.mana = 0
        self.cost = 9999999999
        self.alive = True

    def act(self, my_team, enemy):
        return

    def got_hurt(self, damage):
        if damage >= self.hp:
            self.hp = 0
            self.alive = False
            dprint(self.name + ' died!')
        else:
            self.hp -= damage
            dprint(self.name +
                   f' hurt with remaining hp {self.hp}.')


class Fighter(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Fighter'
        self.max_hp = 1200
        self.hp = 1200
        self.str = 100
        self.cost = 100

    def act(self, my_team, enemy):
        target = rand_alive(enemy)
        dprint(f'Hurt enemy {target} by damage {self.str}.')
        enemy[target].got_hurt(self.str)


class Mage(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Mage'
        self.maxmana = 50
        self.mana = 50
        self.max_hp = 800
        self.hp = 800
        self.cost = 200
        self.int = 400

    def cast(self, my_team, enemy):
        self.mana -= mana_cost
        target = rand_alive(enemy)
        dprint(f'Strike enemy {target} with spell')
        enemy[target].got_hurt(self.int)

    def act(self, my_team, enemy):
        if self.mana < mana_cost:
            self.mana += mana_recovery
            dprint(f'Mana recover to {self.mana}.')
        else:
            self.cast(my_team, enemy)
