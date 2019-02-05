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

# instantiate objects from imported Magic class
fire = Magic("Fire", 10, 30, "dark")
wind = Magic("Wind", 15, 50, "dark")
ice = Magic("Ice", 20, 70, "dark")
magic_list = [fire, wind, ice]
# instantiate objects from imported Person class
player = Person("Knight", 150, 50, 50, magic_list)
enemy = Person("Vampire", 100, 100, 20, magic_list)

# clear terminal and game begins
os.system("cls")

# game title
print("""
###############################
## Welcome to Castle Crawler ##
###############################
""")

# print stats before battle begins
player.stats()
enemy.stats()

# loop starts
running = True
while running:
    print("================")
    print(f"\t {player.name.upper()}")
    print("Choose your action: ")
    player.choose_action()
    choice_input = input("Choose a number >>> ")
    index = int(choice_input) - 1
    print(f"You chose {player.action[index]}")

    # physical attack
    if index == 0:
        dmg = player.generate_atk_damage()
        enemy.take_damage(dmg)
        print("================")
        print(f"You attacked and dealt to {enemy.name} {dmg} points of damage")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose your magic: "))
        magic_index = magic_choice - 1

        magic = player.magic[magic_index]

        # generate magical damage
        magic_damage = magic.generate_magic()
        magic_name = magic.name
        magic_cost = magic.mp_cost

        #check if player has enough MP to use
        if magic_cost > player.mp:
            print("not enough MP")
            continue

        else:
            player.reduce_mp(magic_cost)
            enemy.take_damage(magic_damage)
            print("================")
            print(f"You attacked with {magic_name} and dealt to {enemy.name} {magic_damage} points of damage")


    else:
        print("This is easy mode, you cannot choose another option")
        continue

    # enemy turn
    print("================")
    print(f"{enemy.name.upper()}")
    # enemy_choice = random.randrange(0, len(enemy.action))
    enemy_choice = 0
    if enemy_choice == 0:
        enemy_dmg = enemy.generate_atk_damage()
        player.take_damage(enemy_dmg)
        print(f"{enemy.name.capitalize()} attacked and dealt you {enemy_dmg} points of damage")

    # round summary
    print("================")
    player.stats()
    enemy.stats()

    if player.hp == 0:
        print(f"deated by {enemy.name} !")
        running = False
        break
    elif enemy.hp == 0:
        print("You win!")
        running == False
        break
