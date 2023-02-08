from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

order = ''
while order != "off":
    order = input(f"What would you like? ({menu.get_items()})")
    if order == "report":
        coffeemaker.report()
        money_machine.report()
    elif order == "off":
        quit()
    else:
        drink = menu.find_drink(order)
        if coffeemaker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)



