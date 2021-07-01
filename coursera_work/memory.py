# implementation of card game - Memory

import simplegui
import random
deck = ["0", "1", "2", "3", "4", "5", "6", "7"] * 2

# helper function to initialize globals
def new_game():
    global deck, exposed, state, second_click, first_click, turns
    #create new memory order that is diff from last game played
    random.shuffle(deck)
    exposed = [False]*16
    state, second_click, first_click, turns = 0, 0, 0, 0 #can pair variable assignment if assignment is the same
    
     
# define event handlers
def mouseclick(pos):
    global exposed, state, second_click, first_click, turns
    index = list(pos)[0]//50
    
    
    if exposed[index] == False and state == 0: #flipping first card
        exposed[index] = True
        first_click = index
        state = 1
    elif state == 1 and exposed[index] == False: # one card flipped
        second_click = index
        state = 2 
        exposed[second_click] = True
    elif state == 2 and deck[first_click] != deck[second_click]: #two cards flipped
        exposed[first_click], exposed[second_click] = False, False
        state = 0
        turns += 1
        if exposed[index] == False: 
           exposed[index] = True
           state = 1
           first_click = index       
    elif state == 2 and deck[first_click] == deck[second_click]: #two cards flipped
        state = 0
        turns += 1
        if exposed[index] == False: 
           exposed[index] = True
           state = 1
           first_click = index  
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for n in range(16):
        if exposed[n]:
            canvas.draw_polygon([[n*50, 0], [(n+1)*50, 0], [(n+1)*50, 100], [n*50, 100]], 1, "Black", "Yellow")
            canvas.draw_text((deck[n]), (n*50+11, 69), 55, "Black")
        else:
            canvas.draw_polygon([[n*50, 0], [(n+1)*50, 0], [(n+1)*50, 100], [n*50, 100]], 1, "Black", "Green")
    label.set_text("Turns = " + str(turns))
   
    #p = 0
    #canvas.draw_text(deck[0], (p , 75), 100, "Green")
    
    #for number in deck[1:15]:
        #p = p + 53
        #canvas.draw_text(number, (p , 75), 100, "Green")
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric