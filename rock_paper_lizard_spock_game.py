# Rock-paper-scissors-lizard-Spock template

'''
Coursera :Introduction to interactive programming in python part I
Author :Rishabh (uniyalrishabh@gmail.com)
date : December 21, 2019
'''


#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    """
    This helper function assigns number to a string passed to it
    """
    if name == "rock":
        name = 0
        return(name)
    
    elif name == "Spock":
        name = 1
        return(name)
        
    elif name == "paper":
        name = 2
        return(name)
    
    elif name == "lizard":
        name = 3
        return(name)
        
    elif name == "scissors":
        name = 4
        return(name)
        
    else:
        name = "invalid choce"
        return(name)
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    """
    This function converts number to string
    """
    if number == 0 :
        return("rock")
    
    elif number == 1:
        return("Spock")
    
    elif number == 2:
        return("paper")
    
    elif number == 3:
        return("lizard")
    
    elif number == 4:
        return("scissors")
    
    else:
        return("invalid number")
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    '''
    This is the main function to test who wins
    it uses https://www.coursera.org/learn/interactive-python-1/supplement/NlFfP/code-clinic-tips
    to calculate who wins in this game
    '''
    
    # print a blank line to separate consecutive games
    print("\n")

    # print out the message for the player's choice
    print("Player choses : ",player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print("computer choses : ",comp_choice)

    # compute difference of comp_number and player_number modulo five
    mod_diff = (player_number - comp_number)%5
    # use if/elif/else to determine winner, print winner message
    if mod_diff <= 2 and mod_diff>=1:
        print("player wins!")
    
    elif mod_diff >=3 and mod_diff <=4:
        print("computer wins!")
    else:
        print("Tie!")
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



