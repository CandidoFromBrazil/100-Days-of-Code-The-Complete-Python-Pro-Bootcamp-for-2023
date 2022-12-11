#link to game in replit: https://replit.com/@MatheusWillians/Caesar-Cipher?v=1, you can always fork it
#All the project and the inherent libraries are in the additional folder to be downloaded by you, is a folde named: day8.py.zip, enjoy it

#CAESAR CIPHER PROGRAM

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#function responsable for the logical instance 
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  #for used to first: 
  if cipher_direction == "decode":
    shift_amount *= -1
  #for used to first: read all char from the start_text, second: validade if that char is inside the alphabet, third: change the position of the char due to the shift inside the alphabet so as to encode, and lastly, add all the new positions of the char's inside the string(end_text).
  for char in start_text:
    if char in alphabet:
      #check the index from the cchar chosen inside the alphabet
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
#importing the logo
from art import logo
print(logo)

#variable used to control the while loop
should_end = False
while not should_end:
  #lines to as the user whether he wishs to continue or nor to encose and descose the text chosen
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #lil trick used to secure index validation inside the 26 characters in the alphabet list
  shift = shift % 26
  #calling the function caesar
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  #if to keep on the while or quit it, thanks to the bool variable switch(should_end)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    


