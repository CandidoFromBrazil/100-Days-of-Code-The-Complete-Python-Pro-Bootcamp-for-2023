#Banker roulette
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

randomIndex = random.randint(0, len(names))

print(f"{names[randomIndex]} is going to buy the meal today!")
