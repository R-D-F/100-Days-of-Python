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
    "money": 0,
}





def order():
    """Processes drink order, returns MENU[drink]. Turns off machine, or prints report."""
    if drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        return "report"
    return MENU[drink]


def resource_check():
    """Checks resources available against ingredients required"""
    for ingredient in order()['ingredients']:
        if order()['ingredients'][ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        return True


def process_coins():
    """hello"""
    money = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    return money


def check_transaction():
    """hello"""
    if process_coins() > order()["cost"]:
        resources["money"] += order()["cost"]
        change = round(process_coins() - order()["cost"], 2)
        print(f"Here is {change} dollars in change.")
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


def make_coffee():
    """jello"""
    for ingredient in order()['ingredients']:
        resources[ingredient] -= order()['ingredients'][ingredient]
    print(f"Here is your {drink}. Enjoy!")

drink = ""
while drink != "off":
    drink = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order() != "report":
        if resource_check() is not False:
            print("Please insert coins.")
            quarters = int(input("how many quarters?:"))
            dimes = int(input("how many dimes?:"))
            nickles = int(input("how many nickles?:"))
            pennies = int(input("how many pennies?:"))
            process_coins()
            if check_transaction() is True:
                make_coffee()
