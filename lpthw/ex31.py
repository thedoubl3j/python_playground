print("""You enter a dark room with 2 doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. take the cake.")
    print("2. scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your faceoff. Good Job!")
    elif bear == "2":
        print("The bear eats your legs off. Good Job!")
    else :
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss in Cthulu's retina.")
    print("1. blueberries")
    print("2. yellow jacket clothespins")
    print("3. understanding revolvers yelling melodies")

    insanity = input ("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of Jello")
        print("Good Job!")
    else:
        print("The insanity rots your eyes into a pool of muck")
        print("Good Job!")

else:
    print("You stumble around and all on a knife and die.")
