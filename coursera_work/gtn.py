# simplegui is a lib built specifically for this class and only usable inside the classes specific Browser IDE
import simplegui
from random import randrange

secret_number = 0
remaining_guesses = 0
thousand_range = False
# helper function to start and restart the game
def new_game():
    global secret_number
    global remaining_guesses
    if thousand_range:
        secret_number = randrange(0, 1000)
        remaining_guesses = 10
    else:
        secret_number = randrange(0, 100)
        remaining_guesses = 7

# define event handlers for control panel
def rangej():
    # button that changes the range to [0,100) and starts a new game
    global secret_number
    global remaining_guesses
    new_game()
    print ("Game has been reset and new number selected between the range [0, 100)")
    secret_number = randrange(0, 100)
    remaining_guesses = 7
    

def rangek():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global remaining_guesses
    global thousand_range
    thousand_range = True
    new_game()
    print ("Game has been reset and new number selected between the range [0, 1000)")
    secret_number = randrange(0, 1000)
    remaining_guesses = 10
    
def input_guess(guess):
    global remaining_guesses
    guess = int(guess)
    print ("Guess was " + str(guess))
    remaining_guesses = remaining_guesses - 1
    print ("guesses remaining " + str(remaining_guesses))
    if remaining_guesses == 0:
        print ("Out of guesses, game lost")
        new_game()
    elif guess < 0:
        print ("Error: Negative number not accepted. Try again")
    elif guess > secret_number:
        print ("Lower")
    elif guess < secret_number:
        print ("Higher")
    elif guess == secret_number:
        print ("Correct!")
        new_game()
    else:
        print ("error")
        exit()
    
    return guess

    
# create frame
frame = simplegui.create_frame('Guess the Number', 300, 300)

# register event handlers for control elements and start frame
guess = frame.add_input("Your Guess", input_guess, 50)
small_new_range = frame.add_button("Range [0, 100)", rangej)
big_new_range = frame.add_button("Range [0, 1000)", rangek)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric