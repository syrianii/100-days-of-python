### Day 3 assingment

print(
    '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************'''
)

print("Welcome to Treasure Island.\n Your mission is to find the treasure.")

move = input(
    '''You're at a cross road. Where do you want to go? Type "left" or "right"\n'''
).lower()

if move == 'left':
  move = input(
      'You\'ve come to a lake. There is an island in the the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.\n'
  ).lower()
  if move == 'wait':
    move = input(
        'You arrived to the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n'
    ).lower()
    if move == 'yellow':
      print('Congratulation, You Won!!!')
    elif move == 'blue':
      print('You\'ve been eaten by beats. Game Over. ')
    elif move == 'red':
      print('You\'ve been burned by fire. Game Over. ')
    else:
      print('Game Over.')

  else:
    print('You\'ve been attacked by a trout. Game Over')
else:
  print("You've fallen into a hole. \n Game Over. ")
