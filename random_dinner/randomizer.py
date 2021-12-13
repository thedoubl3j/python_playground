import random
from sys import exit

###script to select random meal from a list and then remove it from the selection so that it cannot be picked again
#what do we need
'''
- need meal list
- the thing to select the meal
- thing to remove the selected item from the list

what to do
list already exists, how do we get stuff out of it. 
- a list has elements starting 0 -> n, (1, 2, 3, 4)
- pull random element from list
TODO : next thing is to put the random selection into a function and remove that selection from the list
'''
global dinner
dinner = ['chicken', 'steak', 'pasta', 'veggie']
#print(dinner)
#first_entry = list.pop(dinner, 0)
#print(first_entry)
#def randomizer():
#    random_selection = random.choice(dinner)

def run():
    print("Selecting random dinner from the options list")
    random_selection = random.choice(dinner)
    print (random_selection + " was selected")
    print ("Is this to your liking Clarice?")
    print ("1. Yes")
    print ("2. No")
    answer = input("> ")
    
    if answer == "1":
        print("Then I have nothing else to do, exiting")
        sys.exit()
    elif answer == "2":
        print("Sorry that isn't to your liking, selecting a new dinner")
        random_selection = random.choice(dinner)
        print(random_selection)
        print ("Is this to your liking Clarice?")
        print ("1. Yes")
        print ("2. No")
    else:
        print("input inccorect, try again")
        
run()