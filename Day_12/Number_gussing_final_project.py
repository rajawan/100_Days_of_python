import random
EASY_LEVEL_TURN=10
HARD_LEVEL_TURN=5

#asking user for game level hard or easy

def set_defficulty():
    game_level=str(input("Choose a deficulty type. 'Hard' or 'easy'? ").lower())
    if game_level=='easy':
        return EASY_LEVEL_TURN
    elif game_level=='hard':
        return HARD_LEVEL_TURN
def check_answer(guess,answer,turns):
    if guess>answer:
        print("Guess is too high")
        return turns-1
    elif guess<answer:
        print("Guess is too low")
        return turns-1
    else:
        print("You guess the right answer")
def game():       
    print("Welcome to the number Guessing game in python")
    answer=random.randint(1,100)
    print("I am thinking a number between 1 to 100")
    game_level=str(input("Choose a deficulty type. 'Hard' or 'easy'? ").lower())
    turns=set_defficulty()
    print(f"you have {turns} attempts remaining")
    guess=0
    while guess!=answer:    
        guess=int(input("Make a Guess? "))
        answer=check_answer(guess,answer,turns)
    if turns==0:
        print("You are out of guess. You loss")
        return
    elif guess!= answer:
        print("Guess Again")



game()
