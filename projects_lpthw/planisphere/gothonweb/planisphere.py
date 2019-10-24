class Room(object):
    
    def __init__(self, name, desciption):
        self.name = name
        self.description = desciption
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
# just setting up the variables for each room using the class Room
central_corridor = Room("Central Corridor",
"""
The gothons of the planet percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving member
and your last mission is to get the neutron bomb from the weapons armory, put it on the bridge and blow the ship up after
getting into an escape pod.

You are running down the central corridor to the weapons armory when a gothon jumps out, red scaly skin, dark grimy skin and
evil clown costume flowing around his hate filled body. He is blocking the door to the armory and about to pull a weapon to blast you.""")

laser_weapon_armory = Room("laser weapon armory",
"""
Lucky for you they made you learn gothon insults in the academy. You tell the on gothon joke you know: fasdk some asdfag key strokes
found here yasdflk. The gothon stops, tries not to laugh, then busts out laughing and can't move. While he is laughing, you run up and shoot him square
in the head, putting him down, then jump through the armory door.

)