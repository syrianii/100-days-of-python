print("Welcome to Python pizza deliveries! ")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want to add pepperoni? Y, N ")
add_cheese = input("Do you want to add cheese? Y, N ")

bill = 0

if size == 'S':
  bill += 15
elif size == 'M':
  bill += 20
elif size == 'L':
  bill += 25
  

if (size == 'S') and (add_pepperoni == 'Y'):
  bill += 2
else:
  bill += 3


if add_cheese == 'Y':
  bill += 1


print(f"Your final bill is: ${bill}.")
