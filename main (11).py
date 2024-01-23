from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True
menu_items = menu.get_items()

while is_on:
  
  choice = input(f"What would you like?: ({menu_items}) ")
  
  if choice == 'off':
    is_on = False

  elif choice == 'report':
    coffee_maker.report()
    money_machine.report()

  else:
    menu_item = menu.find_drink(order_name = choice)
    if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
      coffee_maker.make_coffee(menu_item)


    
    
  