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

machine_cash = 0


def print_resources():
    print(f"Water: {resources['water']} \n"
          f"Milk: {resources['milk']}\n"
          f"Coffee: {resources['coffee']}\n"
          f"Cash: {profit}")


def process_coins():
    quarters = int(input("How many quarters do you have "))
    dimes = int(input("How many dimes do you have "))
    nickles = int(input("How many nickles do you have "))
    pennies = int(input("How many pennies do you have "))

    total_inserted = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    print(f"total inserted {total_inserted}")
    return total_inserted


def check_transaction(drink, money):
    drink_cost = drink['cost']
    if drink_cost <= money:
        print("money enough")
        if money > drink_cost:
            print(f"Here is your change of {round(money - drink_cost,2)}")

        return 1
    else:
        print("Sorry that's not enough. Money refunded")
        return 0
# check_transaction('latte',0.52)
profit = 0
def make_coffee(drink):
    resources['water'] -= int(drink['ingredients']['water'])
    resources['milk'] -= int(drink['ingredients']['milk'])
    resources['coffee'] -= int(drink['ingredients']['coffee'])
    global profit
    profit += drink['cost']

def check_resources(drink):
    make_drink = 1
    if resources['water'] < drink['ingredients']['water']:
        print("Sorry there isn't enough water to make this drink")
        make_drink = 0
    if resources['milk'] < drink['ingredients']['milk']:
        print("Sorry there isn't enough milk to make this drink")
        make_drink = 0
    if resources['coffee'] < drink['ingredients']['coffee']:
        print("Sorry there isn't enough water to make this drink")
        make_drink = 0

    return make_drink



print_resources()
stop_coffee_machine = False

while not stop_coffee_machine:
    drink = input("What would you like? (espresso/latte/cappuccino):").lower()
    if drink == 'off':
        stop_coffee_machine = not stop_coffee_machine
    elif drink == 'report':
        print_resources()
    else:
        chosen_drink = MENU[drink]
        if check_resources(chosen_drink) == 1:
            if check_transaction(chosen_drink, process_coins()) == 1:
                make_coffee(chosen_drink)


# TODO: 1. Print a report of all the coffee resources
# TODO: 2. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
print_resources()