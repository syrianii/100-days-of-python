from game_data import data 
from art6 import logo, vs
import random
from replit import clear

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

def format_data(account):
  """format the account data into printable format"""
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(guess, a_follower_count, b_follower_count):
  """take the user guess and follower count and returns if they got it right"""
  if a_follower_count > b_follower_count:
    return guess == 'a'
  else:
    return guess == 'b'
  


while game_should_continue :
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  
  print("Compare A : {format_data(account_a)}")
  print(vs)
  print("Against B : {format_data(account_b)}")
  
  guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
  
  
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear()
  print(logo)
  
  if is_correct:
    score += 1 
    print(f"You're right! Current score {score} ")
  else:
    game_should_continue = False
    print(f"Sorry, you're wrong. Final score {score}")
  