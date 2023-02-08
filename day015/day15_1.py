# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
#     "money": 0,
# }

# # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# # TODO: 1.1. Check the user's input to decide what to do next.
# # TODO: 1.2. The prompt should show every time the action has completed, e.g. once the drink is despensed. The prompt should show again to serve the next customer
# drink = input("What would you like? (espresso/latte/cappuccino):").lower()


# def order():
#     """Processes drink order, returns MENU[drink]. Turns off machine, or prints report."""
#     if drink == "off":
#         quit()
#     elif drink == "report":
#         for resource in resources:
#             print(f"{resource}: {resources[resource]}")
#     else:
#         return MENU[drink]



# # TODO: 2. Turn off the coffee machine by entering "off" to the prompt.
# # TODO: 2.1. For mainteainers of the coffee machine, they can use "off" as a secret word to to turn off the machine. You code should end ececution when this happens
# # TODO: 3. Print report
# # TODO: 3.1. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
# # Water: 100ml
# # Milk: 50ml
# # Coffee: 76g
# # Money: $2.5
# # TODO: 4. Check resurces sufficient?
# def resource_check():
#     """Checks resources available against ingredients required and prints "sorry message" not enough"""
#     for ingredient in order()['ingredients']:
#         if order()['ingredients'][ingredient] > resources[ingredient]:
#             print(f"Sorry there is not enough {ingredient}")
#         else:
#             return True


# # TODO: 4.1. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# # TODO: 4.2. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
# # TODO: 4.3. The same should happen if another resource is depleted, e.g. milk or coffee.
# # TODO: 5. Process coins.

# def process_coins():
#     quarters = int(input("how many quarters?:"))
#     dimes = int(input("how many dimes?:"))
#     nickles = int(input("how many nickles?:"))
#     pennies = int(input("how many pennies?:"))
#     money = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)\
    
#     return money


# # TODO: 5.1. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins
# # TODO: 5.2. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# # TODO: 5.3. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# # TODO: 6. Check transaction successful?
# def check_transaction():
#     if process_coins() > order()["cost"]:
#         resources["money"] += order()["cost"]
#         change = round(process_coins() - order()["cost"], 2)
#         print(f"Here is {change} dollars in change.")
#         return True
#     else: 
#         print("Sorry that's not enough money. Money refunded.")





# # TODO: 6.1. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
# # TODO: 6.2. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# # Water: 100ml
# # Milk: 50ml
# # Coffee: 76g
# # Money: $2.5
# # TODO: 6.3. If the user has inserted too much money, the machine should offer change
# #  E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
# # TODO: 7. Make Coffee.

# def make_coffee():
#     order()
#     resource_check()
#     process_coins()
#     check_transaction()
#     for ingredient in order()['ingredients']:
#         resources[ingredient] -= order()[ingredient]
#     print(f"Here is your {order()}. Enjoy!")

# make_coffee()


# # TODO: 7.1. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
# # E.g. report before purchasing latte:
# # Water: 300ml
# # Milk: 200ml
# # Coffee: 100g
# # Money: $0
# # Report after purchasing latte:
# # Water: 100ml
# # Milk: 50ml
# # Coffee: 76g
# # Money: $2.5
# # TODO: 7.2. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink
