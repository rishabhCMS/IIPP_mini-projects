# template for "Stopwatch: The Game"
import simplegui
import random
import time
# define global variables
#interval = 0
current_time = 0
stop_counter_total = 0
stop_counter_good = 0
is_stopped = True 

# helper function for getting the ratio
def ratio():
    global stop_counter_good, stop_counter_total
    return(str(stop_counter_good) + "/" + str(stop_counter_total))

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(i):
    A = int(i / 600)
    B =int(i / 10)%60
    D = i%10
    if B >= 10:
        return (str(A)+":"+str(B)+"."+str(D))
    elif B< 10:
        return (str(A)+":0"+str(B)+"."+str(D))
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_stopped
    timer.start()
    is_stopped = False

def stop():
    '''
    The if statement is implemented so that the stop counter deon't keep
    on increasing on clicking the stop button when the stopwatch is already
    stopped
    '''
    global stop_counter_total, is_stopped, stop_counter_good
    timer.stop()
    
    if (not is_stopped):
        stop_counter_total += 1
        if current_time % 10 == 0:
            stop_counter_good += 1
    is_stopped = True  
        

def reset():
    global current_time, stop_counter_total, is_stop, stop_counter_good
    timer.stop()
    current_time = 0
    stop_counter_total = 0
    stop_counter_good = 0

# define event handler for timer with 0.1 sec interval
def create_timer():
    global current_time 
    current_time += 1
    print(current_time)

# define draw handler
'''
Event Handler function for drawing the time in seconds
'''
def draw(canvas):
    canvas.draw_text(format(current_time), [100,150], 20, "Red", "sans-serif")
    canvas.draw_text(ratio(),[250, 25], 15, "White", "monospace")
# create frame
frame    = simplegui.create_frame("Stopwatch Game", 300,300)
timer    = simplegui.create_timer(100, create_timer)


# register event handlers
button_1 = frame.add_button("Start", start, 100)
button_2 = frame.add_button("Stop", stop, 100)
button_3 = frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()
#timer.start()
# Please remember to review the grading rubric
