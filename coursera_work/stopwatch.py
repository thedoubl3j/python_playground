import simplegui
# define global variables
seconds = 0
totalStops = 0
goalStop = 0
isRunning = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(n):
    A = n // 600
    e = n // 10 
    f = e % 60 
    B = f // 10
    C = f % 10
    D = n % 10
    
    return str(A) + ":" + str(B) + str(C) + "." + str(D) 
    
# handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global isRunning
    timer.start()
    isRunning = True

def stop_handler():
    global isRunning, totalStops, goalStop
    timer.stop()
    if isRunning:
        totalStops += 1
    else:
        pass
    
    if seconds % 10 == 0 and seconds != 0:
        goalStop += 1
    isRunning = False
    
def reset_handler():
    global seconds, isRunning, totalStops, goalStop
    timer.stop()
    totalStops = 0
    goalStop = 0
    seconds = 0
    isRunning = False

#score 
def score():
    global totalStops, goalStop
            
    return str(goalStop) + "/" + str(totalStops)

# timer and draw handlers
def tick():
    global seconds
    seconds = int(seconds)
    seconds = seconds + 1
    

def draw_handler(canvas):
    global seconds
    #seconds = str(seconds)
    canvas.draw_text((format(seconds)), (120, 150), 24, 'White')
    canvas.draw_text((score()), (250, 20), 20, 'White')
    
    
# create frame
frame = simplegui.create_frame("Timer", 300, 300)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw_handler)
start = frame.add_button('Start', start_handler)
stop = frame.add_button('Stop', stop_handler)
reset = frame.add_button('Reset', reset_handler)


# start frame
frame.start()
