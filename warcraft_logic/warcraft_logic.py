#!/usr/bin/env python
""'put all of this into a fucntion"""
def main():
    print("""The Warcraft faction game.
    Choose your faction.""")
    print("1. Horde")
    print("2. Alliance")
    #select the factions
    faction = input("> ")
    #horde logic tree, finish out the "no orc" idea
    if faction == "1":
        print("Lok'tar ogar friend. For the Horde!")
        print("What race do you play?")
        print("1. Orc")
        print("2. Not orc")

    horde_race = ("> ")
    if horde_race == "1":
            print("Zug Zug. Orc is best choice for Horde faction")
        elif horde_race == "2":
            print("Why no orc? Bad decision brother")
        else :
            print("Make the right decision, orc is the way to go.")
    elif faction == "2":
        print("Peace be with you friend.")
        print("For the alliance")

    alliance_race == ("> ")
    if alliance_race == "1":
        print("Humans...a great choice.")
        print("Our ancient rivals though...")
    elif alliance_race == "2":
        print("Night Elf, a worthy selection")
        print("The Kaldorei are the elves of the woods")
    else :
        print("What, no I am no orc. Why do you think that?")
        print("Run Thrall, they be onto us")

    else:
        print("You are no part of the eternal conflict?")
        print("Good. Best to stay out of it, it not pretty")
        print("If you do join though, horde orcs is where you should go")

if __name__ == '__main__':
    main()
