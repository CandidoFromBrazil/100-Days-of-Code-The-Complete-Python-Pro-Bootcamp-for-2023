#Rock, paper, scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

handImages = [rock, paper, scissors]

userChoice = int(input('Chose 0 to "rock", 1 to "paper", 2 to "scissors"\n'))

#win/lose logical algorithm
if userChoice >= 3 or userChoice < 0:
  print("You typed an invalid number, you lose!")
else:
  #user choice logic
  print("Player chose:")
  print(f"{handImages[userChoice]}")

  #computer choice logic
  print("Computer chose:")
  computerChoice = random.randint(0, 2)
  print(f"{handImages[computerChoice]}")

  if userChoice == 0 and computerChoice == 2:
    print("You win!")
  elif computerChoice == 0 and userChoice == 2:
    print("You lose")
  elif computerChoice > userChoice:
    print("You lose")
  elif userChoice > computerChoice:
    print("You win!")
  elif computerChoice == userChoice:
    print("It's a draw")
