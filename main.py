from sys import stdout
import sys
import game
from time import sleep
from game import Person
from random import randint
from random import randrange
import random
import time
import os
import textwrap
from magic import Magic


os.system("cls")

print("""
###############################
## Welcome to Castle Crawler ##
###############################
""")

fire = Magic("Fire", 10, 30, "dark")
wind = Magic("Wind", 15, 50, "dark")
ice = Magic("Ice", 20, 70, "dark")
magic_list = [fire, wind, ice]



good = Person("Knight", 150, 50, 50, magic_list)
bad = Person("Vampire", 100, 100, 20, magic_list)

good.stats()
bad.stats()

running = True

print("\nA Vampire attacks!")
while running:
    print("================")
    print("Choose your action: ")
    good.choose_action()
    choice = int(input(">>> "))
    action_index = choice - 1
    if action_index == 0:
        damage = good.generate_dmg()
        bad.take_dmg(damage)

        print("You attacked {} and dealt {} damage".format(bad.name, damage))
    if action_index == 1:
        good.choose_magic()
        magic_choice = int(input(">>> "))

    else:
        print(" Choose a correct number")
        continue

    bad_choice = 0
    if bad_choice == 0:
        enemy_dmg = bad.generate_dmg()
        good.take_dmg(enemy_dmg)
        print("{} attacked {} and dealt {} damage".format(bad.name, good.name, enemy_dmg))


    good.stats()
    bad.stats()


    if good.hp() == 0:
        print("You've been defeated")
        running = False
    elif bad.hp() == 0:
        print("You've been defeated by the Vampire")
        running == False
