

with open('Input/Names/invited_names.txt') as names_file:
  names = names_file.readlines()

with open('Input/Letters/starting_letter.txt') as letter_file:
  letter = letter_file.read()
  



for name in names:
  
  new_letter = letter
  stripped_name = name.strip()
  new_letter = new_letter.replace('[name]',stripped_name)
  with open(f'Output/ReadyToSend/letter_to_{stripped_name}.txt', 'w') as letter_file:
    letter_file.write(new_letter)
  

  
