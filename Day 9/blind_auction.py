from replit import clear
from art2 import sign 

other_biders = True
bids = {}
max_bid = 0
winner_bid = ''

print(sign)

while other_biders:
  name = input("What's your name? \n")
  names_bid = input("What's your bid? \n")
  bids[name] = names_bid
  answer = input("Are there any other biders? Type 'yes' or 'no'.")
  if answer == 'no':
    other_biders = False
  clear()

for name in bids:
  bid = int(bids[name])
  if bid > max_bid:
    max_bid = bid 
    winner_bid = name

print(f'The winner bid is {winner_bid} with a bid of {max_bid}$')
