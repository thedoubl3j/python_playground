#wip
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
if faction == "2":
    print("Peace be with you friend.")
    print("For the aliance")





#allianca logic tree. something punny about the boy king could work and also maybe dive one more layer deeper or add something else.
