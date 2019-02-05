
import random

class Magic:
    """
    this Magic has name, mp cost, dampage, type
    """
    def __init__(self, name, mp_cost, damage, magic_type):
        self.name = name
        self.mp_cost = mp_cost
        self.damage = damage
        self.magic_type = magic_type
        self.high_damage = damage + 15
        self.low_damage = damage - 15

    def generate_magic(self):
        damage = random.randrange(self.low_damage, self.high_damage)
        return damage
