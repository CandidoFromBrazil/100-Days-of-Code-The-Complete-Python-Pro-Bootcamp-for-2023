# Link Beeborn's Leasson hurdle 4: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

def jump2():
  if wall_in_front():
    turn_left()
  if wall_on_right():
    while wall_on_right() == True:
      move()
  if is_facing_north():
    turn_right()
    move()
    turn_right()
    move()
    while wall_on_right() == True and front_is_clear():
      move()
    turn_left()

def theWhile():
  if wall_in_front():
    jump2()
  else:
    move()
