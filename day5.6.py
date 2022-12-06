#Love calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combinedString = name1 + name2
lowerstring = combinedString.lower()

t = lowerstring.count("t")
r = lowerstring.count("r")
u = lowerstring.count("u")
e = lowerstring.count("e")
true = t + r + u + e

l = lowerstring.count("l")
o = lowerstring.count("o")
v = lowerstring.count("v")
e = lowerstring.count("e")
love = l + o + v + e

loveScore = int(str(true) + str(love))

if (loveScore < 10) or (loveScore > 90):
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (loveScore >= 40) and (loveScore <= 50):
  print(f"Your score is {loveScore}, you are alright together")
else:
  print(f"Your score is {loveScore}.")
