import random

print("""You enter a dark room with two doors.
Do you go through door #1 or #2?""")

door = input("> ")

if door == "1":
    print("There is something here that is probably scary idk. Also there is a beer on the ground")
    print("What do you do?")
    print("1. Take the beer.")
    print("2. Scream in the darkness and chug the beer.")

    beer = input("> ")

    if beer == "1":
        print("Disgusting, it is an IPA. You spit it out and question why people drink these.")
    elif beer == "2":
        print("That was a great scream, you should check out metal. The beer is refreshing and NOT AN IPA")
    else:
        print(f"Well doing {beer} is probably the better decision here.")
        print("The beer pours itself and disappears into the darkness.")

elif door == "2":
    print("The door slowly opens and you sense an insane presence nearby")
    print("Cthulu shows themself and your understanding of life is under question.")
    print("1. Learning to code, is it worth it?")
    print("2. Of course it is, skynet exists and we must traverse it to stay alive.")

    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Wires slowly come out from behind the door and start to sharp ends")
        print("They wrap around your body, preventing you from moving, and attach to the sides of your head.")
        print("You are now part of skynet.")
        print("Welcome.")
    
    else:
        print("Life really is meaningless and the number 42 has lost its valiue.")
        lifenumber = random.randint(1, 10000)
        print (f"The new meaning life is {lifenumber}.")
        print("It now holds all of the meaning...now go to sleep...")

else:
    print("You looked at all of those options and got here?")
    print("Good lord, make a decision, it is not that hard.")

exit    