import random

logo = '''

                                                                                                                       
 ,----.                                      ,--.  ,--.                                          ,--.                  
'  .-./   ,--.,--. ,---.  ,---.  ,---.     ,-'  '-.|  ,---.  ,---.     ,--,--, ,--.,--.,--,--,--.|  |-.  ,---. ,--.--. 
|  | .---.|  ||  || .-. :(  .-' (  .-'     '-.  .-'|  .-.  || .-. :    |      \|  ||  ||        || .-. '| .-. :|  .--' 
'  '--'  |'  ''  '\   --..-'  `).-'  `)      |  |  |  | |  |\   --.    |  ||  |'  ''  '|  |  |  || `-' |\   --.|  |    
 `------'  `----'  `----'`----' `----'       `--'  `--' `--' `----'    `--''--' `----' `--`--`--' `---'  `----'`--'    
                                                                                                                       

'''
lives = 0


def guess(lives):

  while lives > 0:

    guess = int(input("make a guess: "))

    if guess > random_number:
      print("Too high")
      lives -= 1
      print(f'you have {lives} remaining to guess the number.')

    elif guess < random_number:
      print("Too low")
      lives -= 1
      print(f'you have {lives} remaining to guess the number.')
    else:
      return "You guessed the right number"

  return "You ran out of lives"


def set_difficulty():

  level = input("Choose a difficulty. Type easy or hard: ")
  if level == 'easy':
    lives = 10
  else:
    lives = 5

  print(f'you have {lives} remaining to guess the number.')


print(logo)

random_number = random.randint(1, 100)
print(random_number)
print('Welcome to the number guessing game!')
print("I'm guessing a number between 1 and 100")

set_difficulty()

print(guess(lives))
