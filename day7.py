#link to game in replit: https://replit.com/@MatheusWillians/Day-7-Hangman-Final?v=1, you can always fork it
#importing librarys
import random
from hangman_art import logo, stages
from hangman_words import word_list
#for this library to run, apply all the code on https://replit.com/, or just delete this line.
from replit import clear

#random choose of a word
chosen_word = random.choice(word_list)
#variable to control the range(), instead of len() function
word_length = len(chosen_word)

#valiables for control (while)
end_of_game = False
lives = 6

#logo print
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#while for re-validation over guess
while not end_of_game:
  #input for guess
    guess = input("Guess a letter: ").lower()
    #clear function called from the replir library, must be delected with the library as well
    clear()
    #"no repeated guess"
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #conveying the stages of our handman
    print(stages[lives])
