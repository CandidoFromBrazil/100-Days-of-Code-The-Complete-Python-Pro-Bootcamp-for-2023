#Number Guessing Game 


#Importing libraries 
from random import randint
from Logo import logo as logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#responsable for checking if the guess is the same as the answer, and keep track of the turns left to guess
def check_aswer(guess, answer, turns):
    """Checks answer agains guess, returns the number os turns left"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif(guess < answer):
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was: {answer}.")

#responsable for recieve the difficulty choise from the player and assingn it to be use later
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else: 
        return HARD_LEVEL_TURNS    

#functio game is the game-itself, the playable structure
def game():
    #first instroduction
    print(logo)
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    #random answer choise 
    answer = randint(1, 101)

    #turns is the return of the set_difficulty() function, created previously
    turns = set_difficulty()

    #while responsable for the loop that keeps the game playable
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #asks a guess from the player
        guess = int(input("Make a guess: "))

        #turns is re-assingn within the while loop so as to keep the counter (turns) accurate with the remaining turns to guess
        turns = check_aswer(guess, answer, turns)
        #checks per-loop if the amount of guesses has overdone itself
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")
game()