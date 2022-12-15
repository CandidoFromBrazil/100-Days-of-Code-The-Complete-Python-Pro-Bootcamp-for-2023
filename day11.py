# link to game in replit: https://replit.com/@MatheusWillians/Blackjack?v=1, you can always fork it
# All the project and the inherent libraries are in the additional folder to be downloaded by you, is a folde named: day11.py.zip, enjoy it

#Blackjack Game

import random
from replit import clear
from art import logo


#function to choce a random card from cards list
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


    #function to sum all cards in hands, for each hand
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    #if mannaged to lookup for a blackjack (21)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #if mannaged to remove 11 and replace it as a ace, after score over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


#score comparation function
def compare(user_score, computer_score):
    #Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


#function to start out the game
def play_game():

    print(logo)

    #list to append the deal cards either for the user and computer
    user_cards = []
    computer_cards = []
    #control boolean
    is_game_over = False

    #for tho assign two new card inside our lists above
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        #scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        #user's logic to play
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #computer's logic to play
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"   Computer's final hand: {computer_cards}, final score: {computer_score}"
    )
    print(compare(user_score, computer_score))


#third while, responsable for keep the game going on
while input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
