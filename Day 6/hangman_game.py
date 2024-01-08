import random
from hangman_stages import stages, logo
from hangman_word import word_list
from replit import clear

print(logo)
chosen_word =  random.choice(word_list)
ciphered_word = ''
print(chosen_word)
end_of_game = False
lives = 6

for i in range(len(chosen_word)):
  ciphered_word += '-'

print(ciphered_word)

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  if guess in ciphered_word:
        print(f"you already chosen {guess}")
        print(ciphered_word)
  
  for position in range(len(chosen_word)):
      letter = chosen_word[position]
      ciphered_word = list(ciphered_word)
      if guess == letter:
       
        ciphered_word[position] = letter
        print(ciphered_word)
     
  if "-" not in ciphered_word:
    end_of_game = True
    print("You won!!")

  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed the letter {guess}, that's not in the word, you lose a life.")
    print(stages[lives])
    if lives == 0:
      end_of_game = True 
      print('You Lose !')


