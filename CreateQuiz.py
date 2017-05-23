
    #Create your own quiz game Nanodegrees "intro to Programming"
quiz_questions = {'easy':
"""Total of ___1___ players make up a soccer team for competetive game. 
There are total of ___2___ players starting for one 
team in the NBA game. ___3___ is the head coach for the New England Patriots. 
The 2014 FIFA world cup was held in ___4___. 
 Lebron James plays for the ___5___ in the 2016 NBA finals.""",
        'medium':
"""___1___ won the F.I.F.A world cup in 2006. 
Two countries ___2___ and ___3___ jointly hosted the 2002 FIFA World Cup. 
NBA team __4__ is know "the Red Oxen" in China. 
New England Patriots have won total of ___5___ Superbowl rings""",
        'hard':
"""___1___ is one of the players who have appeared in five FIFA World Cup Finals
tournaments each. ____2____ was the only manager to win the FIFA World Cup twice. 
An award named Rookie of the year in the NBA is named after Eddie ___3___. 
In order for NFL players to be eligible for the Pro Football Hall of Fame the 
players must played for at least___4___ years. ___5___ was the first Native 
American language that was broadcast in Superbowl XXX."""}
    
quiz_answers = {'easy': [['11'],['5'],['Belichick','Belichick'],['brazil', 'Brazil'],
                         ['Cleveland','Cavaliers','Cavs']],
            'medium': [['Italy'],['Japan'],['Korea'],['bulls', 'Bulls'],['5']],
            'hard': [['Matthaus'],['Japan', 'japan'],['Gottlieb'],['Ghibli'],
                    ['5'],['Novajo', 'novajo']]}
    

def welcome():
	''' Prints a greeting statment'''
	print( "Hello! Welcome to sports Quiz and lets have fun!!")
    
def set_level():
    """ Sets the quiz ``difficulty`` level. """
    global game_mode
    game_mode= input("Please select the level of difficulty: \neasy, medium, or hard-->")
    while game_mode not in quiz_questions:
        game_mode = input("Please select the level of difficulty: \neasy, medium, or hard-->")

    print ("\nYou chose level - " + game_mode)
    
def num_attempts():
    """ Fucntion sets the number of attempts per question. """
    global attempts

    attempts = input("How many attempts would you like per question:  ")
    while not attempts.isdigit() or int(attempts) < 1:
        attempts = input("Enter a number that is greater than 0:  ")
    attempts = int(attempts)
    
def answer_checker(option, user_guess):
    """ Functions check answers
        option: List of possible answers for question.
        user_guess (string): number of possible user_guess for quiz question.
    """
    for answer in option:
        if user_guess.lower() == answer.lower():
            return True
        else:
            False

def fill_in_answers(index, player_answer):
    """ This function get players input for blank number which I assinged 'index'.
   The global variable level becomes false when user used up all their chances.
        player_answer is string and updated with the user's answer.
    """
    #level = True
    global level
    possible = attempts
    answer = quiz_answers[game_mode][index]
    print ([game_mode])
    print ([index])

    while possible > 0:
        guess = input("What goes in ___%s___: " % str(index+1))
        if answer_checker(answer, guess):
            print ("Correct! Good Job! \n")
            player_answer = player_answer.replace('___%s___' % str(index+1), guess)
            print (player_answer)
            break
        elif possible > 1:
            print ("\nYour answer was incorrect. Please try again.\n")
            possible += -1 #decrease the number of attempt everytime user attempt incorrectly
            print (possible, "attempt remaining! \n")
        else:
            #return 0
            level = False
            break
    return player_answer

def game_start():
    """ This function shows the quiz and ask the user for answers
    I used boolean function to declare whether the user completes the quiz if its TRUE
    and FALSE if the user attempt too many times. 
    """
    # calling fucntions from above 
    welcome()
    set_level()
    game = quiz_questions[game_mode]
    num_attempts()
    print (game)
    
    #declarations of global variables 
    global level
    level = True
    global range
   
    for index in range(len(quiz_answers[game_mode])):
        game = fill_in_answers(index, game)
        if not level: 
            break

    if level:
        print ("YAY, You did it!\n")
    else:
        print ("\n You are out of attemps\n")
        print ("Game Over")
        
    return level
    
# Main 
if __name__ == '__main__':    
    
    while True:
        game_start()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    