# __init__ initialzies object
# object oriented programming
from random import randint
from random import randrange
import random

class Person:
    def __init__(self, name, hp, mp, atk):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.action = ["Physical Attack", "Magic"]
        self.magic = magic


    def stats(self):
        print(self.name)
        print(f"{self.hp}/{self.maxhp}")
        print(f"{self.mp}/{self.maxmp}")


    def generate_dmg(self):
        dmg = random.randint(self.atk_low, self.atk_high)
        return dmg


    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp


    def get_hp(self):
        return self.hp


    def get_maxhp(self):
        return self.maxhp


    def choose_action(self):
        index = 1
        print("ACTIONS: ")
        for element in self.action:
            print("{}. {}".format(index, element))
            index = index + 1

    def reduce_mp(self, used_mp):
        self.mp = self.mp - used_mp
        if self.mp < used_mp:
            print("not enough Mana")
        return self.mp


    def choose_magic(self):
        index = 1
        print("Choose magic: ")
        for element in self.magic_list:
            print("{}. {}. {}.".format(index, element))
            index = index + 1
