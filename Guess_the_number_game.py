# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

count = 0
trial = 0
secret_number = 0 
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, count, trial
    count = math.ceil(math.log(100 - 0 + 1)/math.log(2))
    trial = math.ceil(math.log(100 - 0 + 1)/math.log(2))
    secret_number = random.randrange(0, 100)
    
    print("\n ----Starting new game-----")
    
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game()
    global secret_number, count, trial
    count = math.ceil(math.log(100 - 0 + 1)/math.log(2))
    trail = math.ceil(math.log(100 - 0 + 1)/math.log(2))
    secret_number = random.randrange(0, 100)
    
    print("----starting game with a new guess range [0,100)-----trials left = ", trial, "\n")
    print("intializing new secret number b/w [0, 100) for you to guess \n")
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game()
    global secret_number, count, trial
    count = math.ceil(math.log(1000 - 0 + 1)/math.log(2))
    trial = math.ceil(math.log(1000 - 0 + 1)/math.log(2))
    secret_number = random.randrange(0, 1000)
   

    print("----starting game with a new guess range [0,1000)-----trials left = ", trial, "\n")
    print("intializing new secret number b/w [0, 1000) for you to guess \n")
    
def input_guess(guess):
    # main game logic goes here
    global trial
    trial = trial - 1
    print("trials left ", trial)
    guess = int(guess)
    print("Guess was: ", guess)
    
    if guess < secret_number and trial != 0:
        print("Guess something higher")
    
    elif guess > secret_number and trial != 0:
        print("Guess something lower")
        
    elif trial == 0:
        print("you lost, trials over!")
        if count  == 7:
            range100()
        else:
            range1000()
        
    elif guess == secret_number:
        print("correct guess!")
        print("the secret number was :", secret_number)
        if count == 7:
            range100()
        else:
            range1000()

    
# create frame
frame = simplegui.create_frame("guess the number", 300, 300) 

# register event handlers for control elements and start frame
frame.add_input("enter your guess", input_guess, 200)
frame.add_button("Restart game!", new_game, 200)
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
