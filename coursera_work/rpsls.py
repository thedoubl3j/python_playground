import random

# helper functions

def name_to_number(name):
    # names to numbers conversion
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "Error: name not found in RPSLS."
    
    return number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # now numbers to names
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "Error: number not found in range"
        
    return name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
                                   
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    
    # compute difference of player_number and comp_number modulo five
    winner = (comp_number - player_number) % 5

    # use if/elif/else to determine winner
    if winner < 3:
        player_win = False
    else:
        player_win = True 
    
    #another if block to print winner or tie
    if player_win:
        print "Player wins!"
    elif comp_number == player_number:
        print "Player and computer tie!"
    else:
        print "Computer wins!"
    #print blank line for next game
    print 
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric