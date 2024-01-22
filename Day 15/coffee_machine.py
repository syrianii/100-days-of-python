
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
is_on = True

def is_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    num_of_quarters = float(input("How many quarters?: "))
    num_of_dimes = float(input("How many dimes?: "))
    num_of_nickles = float(input("How many nickles?: "))
    num_of_pennies = float(input("How many pennies?: "))
    total = (num_of_quarters * 0.25) + (num_of_dimes * 0.10) + (num_of_nickles * 0.05) + (num_of_pennies * 0.01)
    return total

def transaction_succeed(payment,cost):
    global profit
    if payment < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False

    elif payment == cost:
        profit += payment
        return True

    else:
        refund = payment - cost
        print(payment)
        profit += payment
        print(f"Here is ${round(refund,2)} dollars in change")
        return True

def make_coffee(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]




while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == 'off':
        is_on = False

    elif choice == 'report':
        water = resources['water']
        milk = resources['milk']
        coffee = resources['coffee']
        print(f"Water : {water}ml \n"
              f"Milk : {milk}ml \n"
              f"Coffee : {coffee}g \n"
              f"Money : {profit}$ ")

    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingredients']):
            payment = process_coins()
            if transaction_succeed(payment,drink['cost']):

                make_coffee(drink['ingredients'])
                print(f"Here is your {choice} . Enjoy!")






