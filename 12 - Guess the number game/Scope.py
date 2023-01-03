################### Scope ####################

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")


#Local Scope
def drink_Potion():
  potion_strenght = 2
  print(f"local scope: {potion_strenght}")
drink_Potion()

#Global Scope
player_helth = 10
def game():
    def drink_Potion_global():
        potion_strenght = 2
        print(f"global scope: {player_helth}")
    drink_Potion_global()
game()

#Modifying global scope
enemies = 1
def increase_enemies_global():
    print(f"enemies inside function: {enemies}")
    return enemies + 4
enemies = increase_enemies_global()
print(f"enemies outside function: {enemies}")

#Global constant
PI = 3.14
URL = "https://github.com/CandidoFromBrazil"