# __init__ initialzies object
# object oriented programming
from random import randint
from random import randrange
import random

class Person:
    def __init__(self, name, hp, mp, atk, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk_high = atk + 15
        self.atk_low = atk - 15
        self.action = ["Attack", "Magic"]
        self.magic = magic
        self.name = name




    def generate_atk_damage(self):
        """
        randomly generate an attack range within
        atk_low and atk_high and return value
        """
        dmg = random.randrange(self.atk_low, self.atk_high)
        return dmg


    def take_damage(self, dmg):
        """
        hp will decrease when player takes dampage
        when hp drops below 0, it will = 0
        """
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp


    def choose_action(self):
        """
        This method triggers a list of attack options
        """
        number = 1
        print("ACTIONS: ")
        for element in self.action:
            print(f"{number}: {element}")
            number = number + 1


    def stats(self):
        """
        maxhp will never be altered
        """
        print(self.name)
        print(f"{self.hp}/{self.maxhp}")
        print(f"{self.mp}/{self.maxmp}")



    def reduce_mp(self, cost):
        """
        calculate and return new mp after magic attack
        """
        self.mp = self.mp - cost
        return self.mp


    def choose_magic(self):
        """
        prints a list of magic attacks
        """
        number = 1
        print("Choose magic: ")
        for element in self.magic:
            print(f"{number}. {element.name}")
            number = number + 1
