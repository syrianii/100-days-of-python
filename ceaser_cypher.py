from art import sign

alphabet =  ['a','b','c','d','e','f','g','h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
play = True
def cipher(text,shift,direction):
  new_text = ''
  
  if direction == 'decode':
      shift *= -1
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift
      if new_position > len(alphabet):
        letter = alphabet[len(alphabet) - new_position ]
      elif new_position < 0:
        letter = alphabet[new_position + len(alphabet)]
      else:
        letter = alphabet[new_position]
    new_text += letter
    
  print(new_text)




      
      
      
print(sign) 
while play == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  cipher(text,shift,direction)
  answer = input("Type 'yes' if you want to go again,otherwise type 'no'.\n")
  if answer == 'no':
    play = False
    print('Goodbye!')