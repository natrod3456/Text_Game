#########################################
# contains all weapons
# @Author Natalie Rodriguez
# @version Winter 2018
#########################################
import random

class Weapon(object):
    def __init__(self, name, modifier, durability):
        self.name = name
        self.modifier = modifier
        self.durability = durability

class HersheyKiss(Weapon):
    def __init__(self):
        Weapon.__init__(self, "HersheyKiss", 1, -1)

class SourStraw(Weapon):
    def __init__(self):
        Weapon.__init__(self, "SourStraw", random.uniform(1.00, 1.75), 2)

class ChocolateBar(Weapon):
    def __init__(self):
        Weapon.__init__(self, "ChocolateBar", random.uniform(2.00, 2.40), 4)

class NerdBomb(Weapon):
    def __init__(self):
        Weapon.__init__(self, "NerdBomb", random.uniform(3.50, 5.00), 1)