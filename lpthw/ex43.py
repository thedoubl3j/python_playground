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
        pass

class TheBridge(Scene):

    def enter(self):
        pass

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
