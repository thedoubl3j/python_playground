#!/usr/bin/env python
from sys import exit

"""everything is in a function but it isn't starting properly"""
def start():
    print("""The Warcraft faction game.
    Choose your faction.""")
    print("1. Horde")
    print("2. Alliance")
    #select the factions
    faction = input("> ")
    if faction == "1":
        horde_faction()
    elif faction == "2":
        alliance_faction()
    else:
        no_part()


def horde_faction():
    print("Lok'tar ogar friend. For the Horde!")
    print("What race do you play?")
    print("1. Orc")
    print("2. Not orc")

    horde_race == ("< ")
    if horde_race == "1":
        print("Zug Zug. Orc is best choice for Horde faction")
    elif horde_race == "2":
        print("Why no orc? Bad decision brother")
    else:
        print("Make the right decision, orc is the way to go.")

def alliance_faction():
    print("Peace be with you friend")
    print("1. Human")
    print("2. Night Elf")
    print("3. Something seems suspect here...")
    print("4. I take no part in the conflict.")

    alliance_race = ("> ")
    if alliance_race == "1":
        print("Humans...a great choice.")
        print("Our ancient rivals though...")
    elif alliance_race == "2":
        print("Night Elf, a worthy selection")
        print("The Kaldorei are the elves of the woods")
    elif alliance_race == "3":
        print("What, no I am no orc. Why do you think that?")
        print("Run Thrall, they be onto us")
    else:
        no_part()

def no_part():
    print("You are no part of the eternal conflict?")
    print("Good. Best to stay out of it, it not pretty")
    print("If you do join though, horde orcs is where you should go")

if __name__ == '__start__':
    start()
