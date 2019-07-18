from sys import exit
from random import randint
from textwrap import dedent

# this is the base scene class
class Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You Died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that is better at this than you.",
        "You're worse than your Dad's jokes."

]

    def enter(self):
        print(Death.quips[randint90, len(self.quips)-1])
        exit(1)
class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Gothons of the Planer Percal number 25 have invaded your ship and destroyed your entire crew. You are the last surviving member and your last missing is to get to the neutron destruct
        bomb from the Weapons Armory, put it in the bride and blow the ship up after getting into an escape pod.

        You're running down the central corridor to the weapons armory when a Gothon jumps out, red scaly skin, dark grimy teeth and evil clown costume flowing around his hate
        filled body. He is blocking the door to the armory and about to pull a weapon to blast you.
        """))

        action = input("> ")
        if action == "shoot!":
            print(dedent("""
                  Quick on the draw, you yank out ypour blaster and fire at the Gothon. His clown costume is flowing and moving around his body which throws off your aim.
                  Your laser hits his costume but misses him entirely. Thie completely ruins his costume that his mother bought him,. Which enrages him even more and causes him to blast you
                  in the face until you are dead. After that, he consumes your withering soul.
            """))
            return 'death'

        elif action == "Dodge!":
            print(dedent("""
                Like a world class boxzer, you dodge weave, slip and slide past shots coming your way. ONly in the middle of the moves do you slip and crack your head on the floor then pass out.
                You wake up only to get crushed by the gothon and then eaten.
                """))
                return 'death'

        elif action == "tell a joke":
            print(dedent("""
                  Luckily for you, they made you learn Gothon insdules in the academy. You the one gothon joke you know: existence is pain, wuba luba dub dub.
                  The gothon stops, tries not to laugh then breaks out cry laughing, startling you because that noise reminds you of a distant past.
                  Anywho, you go up, shoot him in the head a point blank range and get to the missle room.
                  """))
                return 'laser_weapon_armory'

        else:
            print("Incorrect, please try again useless human.")
            return 'cental_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
              You do a dive roll into the Weapon Armory, crouch and scan the room for Gothons that might be hiding. It's dead quiet, to quiet. You stand up and run to the far side of the room and
              find the neutron bomb in its container.

              There's a keypad lock on the box and you need the code to get into it. If you get the code wrong 10 times then the lock closes forever and you can never get the bomb out. The code is 3 digits.
              """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
            The container clicks open and the seal breaks, letting out a small whisp of gas out. You grab the neutron bomb and run as fast as 
            you can to the bridge where you must place it in the right spot. 
            """))
            return 'the_bridge'
        else:
            print(dedent("""
            The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together. You sit there, sad at your loss. 
            Then, when the cripling existential dread sets in, you end it all before the gothons can.
            """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        You burst onto the brudge with the neutron bomb under your arm and surprise 5 gothons who are trying to take control of the ship. Each of them has an even uglier clown costume.
        They haven't drawn their weapons yet as they see you are holdingt the bomb and don't want to set it off.  
        """))        

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""In a panic, you throw the bomb at the group of gothons and make a leap for the door. Right as you drop it, a gothon shoots you right in the back killing you.
            As you die, you see another gothon grantically try to disarm the bomb. YOu die knowing the will soon join you. 
            """))
            return 'death'
        
        elif acction == "slowly place the bomb":
            print(dedent("""
            You point your blaster at the bomb under your arm and the gothons put their hands up and start to sweat. 
            """))

class EscapePod(Scene):

        def enter(self):
            pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('cental_corridor')
a_game = Engine(a_map)
a_game.play()
