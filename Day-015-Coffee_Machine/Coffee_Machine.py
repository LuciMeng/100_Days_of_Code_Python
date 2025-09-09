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


WATER = resources['water']
MILK = resources['milk']
COFFEE = resources['coffee']
MONEY = 0

QUARTER = 0.25
DIME = 0.1
NICKLE = 0.05
PENNY = 0.01

def ask_coin():
    """Ask for coin insertion. Generate total monetary value."""
    print("Please insert coins:")
    total = int(input("How many quarters? ")) * QUARTER
    total += int(input("How many dimes? ")) * DIME
    total += int(input("How many nickles? ")) * NICKLE
    total += int(input("How many pennies? ")) * PENNY
    return total

def deduct_resource(water, milk, coffee):
    global WATER, MILK, COFFEE
    WATER -= water
    MILK -= milk
    COFFEE -= coffee
    print(f"There is {WATER}ml water, {MILK}ml milk, and {COFFEE}g coffee left in the machine.")
    return WATER, MILK, COFFEE

def profit(total_coins, coffee_type, cost, water, milk, coffee):
    global MONEY 
    if total_coins < cost:
        print("Not enough money! Money refunded.")
    else:
        change = round(total_coins - cost, 3)
        MONEY += cost # Add profit here
        deduct_resource(water, milk, coffee)
        print(f"Here is ${change} in change. \n"
              f"Here is your {coffee_type} ☕. Enjoy!")

def report():
    """Show current resources level"""
    print(f"Water: {WATER}ml \n"
          f"Milk: {MILK}ml \n"
          f"Coffee: {COFFEE}g \n"
          f"Money: ${MONEY}")

is_on = True

def check_resources(water, milk, coffee):
    """Check if resources are available to make the order."""
    global WATER, MILK, COFFEE
    if WATER < water:
        print("Not enough water!🚰 Money refunded.")
        return is_on == False
    elif MILK < milk:
        print("Not enough milk!🥛 Money refunded.")
        return is_on == False
    elif COFFEE <coffee:
        print("Not enough coffee!🫘 Money refunded.")
        return is_on == False
    else:
        return is_on
      
while is_on:
    order = input("What would you like to order? espresso, latte or cappuccino: \n").lower()

    if order == "report":
        report()

    elif order == 'off':
        print("Machine is now off.")
        is_on = False

    elif order in MENU:
        # Use get() to look for recipe, if it doesn't exist return 0.
        water = MENU[order]["ingredients"].get("water", 0)
        milk = MENU[order]["ingredients"].get("milk", 0)
        coffee = MENU[order]["ingredients"].get("coffee", 0)
        cost = MENU[order]["cost"]
        # check resources
        if check_resources(water, milk, coffee):
            print(f"The price of a {order} is ${cost}.")
            total_paid = ask_coin()
            profit(total_paid, order, cost, water, milk, coffee)

    else:
        print("Invalid input.Try again.")



